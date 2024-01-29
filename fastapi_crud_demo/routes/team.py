import uuid
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud_demo.db import get_session
from fastapi_crud_demo.libs.auth import authenticate
from fastapi_crud_demo.models.team import Team, TeamCreate, TeamUpdate
from fastapi_crud_demo.use_cases import team

router = APIRouter(
    prefix="/api/team",
    tags=["team"],
)


@router.get("/")
async def list_all(
    session: AsyncSession = Depends(get_session), _user: str = Depends(authenticate)
) -> list[Team]:
    return await team.list_all_teams(session=session)


@router.get("/{team_id}", response_model=Team, status_code=HTTPStatus.OK)
async def read(
    team_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
    _user: str = Depends(authenticate),
) -> Team:
    result = await team.read(session=session, team_id=team_id)
    if result is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Team not found")
    return result


@router.post("/", response_model=Team, status_code=HTTPStatus.CREATED)
async def create(
    data: TeamCreate,
    session: AsyncSession = Depends(get_session),
    _user: str = Depends(authenticate),
) -> Team:
    return await team.create(session=session, data=data)


@router.patch("/{team_id}", response_model=Team, status_code=HTTPStatus.OK)
async def update(
    team_id: uuid.UUID,
    data: TeamUpdate,
    session: AsyncSession = Depends(get_session),
    _user: str = Depends(authenticate),
) -> Team:
    result = await team.update(session=session, team_id=team_id, data=data)
    if result is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Team not found")
    return result


@router.delete("/{team_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete(
    team_id: uuid.UUID,
    session: AsyncSession = Depends(get_session),
    _user: str = Depends(authenticate),
) -> None:
    result = await team.delete(session=session, team_id=team_id)
    if result is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Team not found")
