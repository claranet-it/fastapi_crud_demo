from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi_crud_demo.settings import get_settings

settings = get_settings()

engine = create_async_engine(url=settings.database_url, echo=True, future=True)

SessionLocal = async_sessionmaker(
    autocommit=settings.session_auto_commit,
    autoflush=settings.session_auto_flush,
    bind=engine,
)


async def get_session() -> AsyncSession:
    session = SessionLocal()
    try:
        yield session
    finally:
        await session.close()
