import uuid
from http import HTTPStatus

from fastapi import APIRouter

from fastapi_crud_demo.models.team import Team, TeamCreate, TeamUpdate
from fastapi_crud_demo.use_cases import team

router = APIRouter(
    prefix="/api/team",
)


@router.get("/")
async def list_all() -> list[Team]:
    return await team.list_all_teams()


@router.get("/{team_id}")
async def read(team_id: uuid.UUID) -> Team:
    return await team.read(team_id=team_id)


@router.post("/", response_model=Team, status_code=HTTPStatus.CREATED)
async def create(data: TeamCreate) -> Team:
    return await team.create(data=data)


@router.patch("/{team_id}", response_model=Team, status_code=HTTPStatus.OK)
async def update(team_id: uuid.UUID, data: TeamUpdate) -> Team:
    return await team.update(team_id=team_id, data=data)


@router.delete("/{team_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete(team_id: uuid.UUID) -> None:
    return await team.delete(team_id=team_id)
