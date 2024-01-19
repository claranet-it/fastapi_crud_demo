import uuid
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from fastapi_crud_demo.models.team import Team, TeamCreate, TeamUpdate


async def list_all_teams(session: AsyncSession) -> list[Team]:
    result = await session.execute(select(Team))
    teams = result.scalars().all()
    return [Team(**team.model_dump()) for team in teams]


async def read(session: AsyncSession, team_id: uuid.UUID) -> Union[Team, None]:
    result = await session.execute(select(Team).where(Team.id == team_id))
    team = result.scalars().first()
    return Team(**team.model_dump()) if team else None


async def create(session: AsyncSession, data: TeamCreate) -> Team:
    team = Team(**data.model_dump())
    session.add(team)
    await session.commit()
    await session.refresh(team)
    return team


async def update(
    session: AsyncSession, team_id: uuid.UUID, data: TeamUpdate
) -> Union[Team, None]:
    result = await session.execute(select(Team).where(Team.id == team_id))
    team = result.scalars().first()
    if team is None:
        return None

    for field, value in data.model_dump().items():
        if value is not None:
            setattr(team, field, value)
    await session.commit()
    await session.refresh(team)
    return team


async def delete(session: AsyncSession, team_id: uuid.UUID) -> Union[Team, None]:
    result = await session.execute(select(Team).where(Team.id == team_id))
    team = result.scalars().first()
    if team is None:
        return None

    await session.delete(team)
    await session.commit()

    return team
