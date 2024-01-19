import uuid
from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud_demo.db import get_session
from fastapi_crud_demo.models.team import Team, TeamCreate, TeamUpdate
from fastapi_crud_demo.use_cases import team

router = APIRouter(
    prefix="/api/team",
)


@router.get("/")
async def list_all(session: AsyncSession = Depends(get_session)) -> list[Team]:
    return await team.list_all_teams(session=session)


@router.get("/{team_id}")
async def read(
    team_id: uuid.UUID, session: AsyncSession = Depends(get_session)
) -> Team:
    return await team.read(session=session, team_id=team_id)


@router.post("/", response_model=Team, status_code=HTTPStatus.CREATED)
async def create(
    data: TeamCreate, session: AsyncSession = Depends(get_session)
) -> Team:
    return await team.create(session=session, data=data)


@router.patch("/{team_id}", response_model=Team, status_code=HTTPStatus.OK)
async def update(
    team_id: uuid.UUID, data: TeamUpdate, session: AsyncSession = Depends(get_session)
) -> Team:
    return await team.update(session=session, team_id=team_id, data=data)


@router.delete("/{team_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete(
    team_id: uuid.UUID, session: AsyncSession = Depends(get_session)
) -> None:
    return await team.delete(session=session, team_id=team_id)
