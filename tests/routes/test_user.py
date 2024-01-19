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
async def test_login(client: AsyncClient, create_user):
    user = await create_user()

    payload = UserLogin(
        email=user.email,
        password="ZXCV9876,."
    )

    response = await client.post(
        url="/api/user/login",
        content=payload.model_dump_json(),
    )

    assert response.status_code == HTTPStatus.OK
    response_model = response.json()
    assert response_model["access_token"] is not None
    assert response_model["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_user_not_found(client: AsyncClient):
    payload = UserLogin(
        email="wrong-user@email.com",
        password="ASdf12345!."
    )

    response = await client.post(
        url="/api/user/login",
        content=payload.model_dump_json(),
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {"detail": "Login failed"}


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient, create_user):
    user = await create_user()

    payload = UserLogin(
        email=user.email,
        password="wrong-password"
    )

    response = await client.post(
        url="/api/user/login",
        content=payload.model_dump_json(),
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {"detail": "Login failed"}
