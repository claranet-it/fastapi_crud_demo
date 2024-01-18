from settings import get_settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

settings = get_settings()

engine = create_async_engine(url=settings.database_url, echo=True, future=True)


async def get_session():
    session = AsyncSession(engine)
    yield session
