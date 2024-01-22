from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_crud_demo.db import get_session
from fastapi_crud_demo.libs.auth import authenticate
from fastapi_crud_demo.models.error import ErrorResponse
from fastapi_crud_demo.models.token import TokenResponse
from fastapi_crud_demo.models.user import CurrentUser, User, UserCreate, UserLogin
from fastapi_crud_demo.use_cases import user

router = APIRouter(
    prefix="/api/user",
)


@router.post("/register", response_model=User, status_code=HTTPStatus.CREATED)
async def register(
    data: UserCreate, session: AsyncSession = Depends(get_session)
) -> User:
    return await user.register(session=session, data=data)


@router.post("/login", response_model=TokenResponse, status_code=HTTPStatus.OK)
async def login(
    data: UserLogin, session: AsyncSession = Depends(get_session)
) -> TokenResponse:
    login_result = await user.login(session=session, data=data)
    if login_result is None:
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Login failed")

    if isinstance(login_result, ErrorResponse):
        raise HTTPException(status_code=HTTPStatus.FORBIDDEN, detail="Login failed")

    return login_result


@router.get("/me", response_model=CurrentUser, status_code=HTTPStatus.OK)
async def get_current_user(
    session: AsyncSession = Depends(get_session), auth_user: str = Depends(authenticate)
) -> CurrentUser:
    return await user.get_current_user(session=session, email=auth_user)
