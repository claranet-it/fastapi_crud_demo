from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

DATABASE_URL = "postgresql+asyncpg://fastapi_crud_demo:fastapi_crud_demo@localhost:5432/fastapi_crud_demo"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def get_session():
    session = AsyncSession(engine)
    yield session
