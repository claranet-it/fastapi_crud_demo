from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from fastapi_crud_demo.libs.hash_password import create_hash, verify_hash
from fastapi_crud_demo.libs.jwt import create_access_token
from fastapi_crud_demo.models.error import ErrorResponse
from fastapi_crud_demo.models.token import TokenResponse
from fastapi_crud_demo.models.user import User, UserCreate, UserLogin


async def register(session: AsyncSession, data: UserCreate) -> User:
    user = User(
        email=data.email,
        password=create_hash(data.password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def find_by_email(session: AsyncSession, email: str) -> Union[User, None]:
    result = await session.execute(select(User).where(User.email == email))
    user = result.scalars().first()
    return User(**user.model_dump()) if user else None


async def login(
    session: AsyncSession, data: UserLogin
) -> Union[TokenResponse, ErrorResponse, None]:
    user = await find_by_email(session=session, email=data.email)
    if not user:
        return None

    if not verify_hash(data.password, user.password):
        return ErrorResponse(detail="Invalid password")

    return TokenResponse(access_token=create_access_token(user.email))
