from http import HTTPStatus

import pytest
from httpx import AsyncClient

from fastapi_crud_demo.models.user import UserCreate
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
