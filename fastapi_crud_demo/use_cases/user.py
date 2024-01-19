from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud_demo.models.user import UserCreate, User
from fastapi_crud_demo.libs.hash_password import create_hash


async def register(session: AsyncSession, data: UserCreate) -> User:
    user = User(
        email=data.email,
        password=create_hash(data.password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
