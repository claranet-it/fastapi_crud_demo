from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud_demo.db import get_session
from fastapi_crud_demo.models.user import User, UserCreate
from fastapi_crud_demo.use_cases import user

router = APIRouter(
    prefix="/api/user",
)


@router.post("/register", response_model=User, status_code=HTTPStatus.CREATED)
async def register(
    data: UserCreate, session: AsyncSession = Depends(get_session)
) -> User:
    return await user.register(session=session, data=data)

