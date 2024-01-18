import uuid
from http import HTTPStatus

from fastapi import APIRouter

from fastapi_crud_demo.models.team import Team, TeamCreate, TeamUpdate

router = APIRouter(
    prefix="/api/team",
)


@router.get("/")
async def list_all() -> list[Team]:
    return []


@router.get("/{team_id}")
async def read(team_id: uuid.UUID) -> Team:
    return Team(
        id=team_id,
        name="Team 1",
        description="Team 1 description",
    )


@router.post("/", response_model=Team, status_code=HTTPStatus.CREATED)
async def create(team: TeamCreate) -> Team:
    return Team(
        id=uuid.uuid4(),
        **team.model_dump(),
    )


@router.patch("/{team_id}", response_model=Team, status_code=HTTPStatus.OK)
async def update(team_id: uuid.UUID, team: TeamUpdate) -> Team:
    return Team(
        id=team_id,
        **team.model_dump(),
    )


@router.delete("/{team_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete(team_id: uuid.UUID) -> None:
    return
