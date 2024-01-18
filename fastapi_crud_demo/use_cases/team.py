import uuid

from fastapi_crud_demo.models.team import (
    Team,
    TeamCreate,
    TeamUpdate
)


async def list_all_teams():
    return []


async def read(team_id: uuid.UUID) -> Team:
    return Team(
        id=team_id,
        name="Team 1",
        description="Team 1 description",
    )


async def create(data: TeamCreate) -> Team:
    return Team(
        id=uuid.uuid4(),
        **data.model_dump(),
    )


async def update(team_id: uuid.UUID, data: TeamUpdate) -> Team:
    return Team(
        id=team_id,
        **data.model_dump(),
    )


async def delete(team_id: uuid.UUID) -> None:
    return
