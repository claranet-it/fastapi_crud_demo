import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlmodel import SQLModel

from fastapi_crud_demo.db import get_session
from fastapi_crud_demo.main import app
from fastapi_crud_demo.models.team import TeamCreate, Team
from fastapi_crud_demo.settings import get_settings
from fastapi_crud_demo.use_cases import team

settings = get_settings()

engine = create_async_engine(
    url=settings.database_test_url,
    echo=True,
    future=True
)


@pytest_asyncio.fixture(scope="function")
async def session() -> AsyncSession:
    session = async_sessionmaker(
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    async with session() as s:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

        yield s

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def client(session: AsyncSession) -> AsyncClient:
    app.dependency_overrides[get_session] = lambda: session
    async with AsyncClient(app=app, base_url='http://localhost') as client:
        yield client


@pytest.fixture(scope="function")
def create_team(session):
    async def _create_team(name: str = None, description: str = None) -> Team:
        return await team.create(
            session,
            TeamCreate(
                name=name or "Team 1",
                description=description or "Team 1 description"
            )
        )

    return _create_team
