from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from settings import get_settings

settings = get_settings()

engine = create_async_engine(url=settings.database_url, echo=True, future=True)


async def get_session() -> AsyncSession:
    session = AsyncSession(engine)
    yield session
