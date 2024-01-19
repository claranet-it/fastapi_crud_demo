import time
from datetime import datetime, timezone

from fastapi import HTTPException
from jose import JWTError, jwt
from starlette import status

from fastapi_crud_demo.settings import get_settings

settings = get_settings()


def create_access_token(user: str) -> str:
    payload = {"user": user, "expires": time.time() + 3600}

    return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")


def verify_access_token(token: str) -> dict:
    try:
        data = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])

        expire = data.get("expires")

        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token applied",
            )

        if datetime.now(timezone.utc) > datetime.fromtimestamp(expire, timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Access token expired"
            )

        return data

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid access token"
        )
