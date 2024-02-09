from http import HTTPStatus

import pytest
from httpx import AsyncClient

from fastapi_crud_demo.models.user import UserCreate, UserLogin
from fastapi_crud_demo.libs.hash_password import verify_hash


@pytest.mark.asyncio
async def test_register(client: AsyncClient):
    payload = UserCreate(
        email="testuser@email.com",
        password="Asdf1234!!"
    )
    response = await client.post(
        url="/api/user/register",
        content=payload.model_dump_json(),
    )

    assert response.status_code == HTTPStatus.CREATED
    response_model = response.json()
    assert response_model["id"] is not None
    assert len(response_model["id"]) == 36
    assert response_model["email"] == "testuser@email.com"
    assert verify_hash("Asdf1234!!", response_model["password"]) is True


@pytest.mark.asyncio
async def test_token(client: AsyncClient, create_user):
    user = await create_user()

    payload = {
        "username": user.email,
        "password": "ZXCV9876,.",
        "grant_type": "password",
    }

    response = await client.post(
        url="/api/user/token",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    assert response.status_code == HTTPStatus.OK
    response_model = response.json()
    assert response_model["access_token"] is not None
    assert response_model["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_token_user_not_found(client: AsyncClient):
    payload = {
        "username": "wrong-user@email.com",
        "password": "ASdf12345!.",
        "grant_type": "password",
    }

    response = await client.post(
        url="/api/user/token",
        data=payload,
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {"detail": "Login failed"}


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient, create_user):
    user = await create_user()

    payload = {
        "username": user.email,
        "password": "wrong-password",
        "grant_type": "password",
    }

    response = await client.post(
        url="/api/user/token",
        data=payload,
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {"detail": "Login failed"}


@pytest.mark.asyncio
async def test_get_current_user(client: AsyncClient, jwt_token):
    token_response = await jwt_token()

    response = await client.get(
        url="/api/user/me",
        headers={"Authorization": f"Bearer {token_response.access_token}"}
    )

    assert response.status_code == HTTPStatus.OK

    response_model = response.json()
    assert response_model["id"] is not None
    assert len(response_model["id"]) == 36
    assert response_model["email"] == "tester@email.com"
