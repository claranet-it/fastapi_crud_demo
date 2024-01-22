from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status

from fastapi_crud_demo.libs.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/user/token")


async def authenticate(token: str = Depends(oauth2_scheme)) -> str:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Missing access token"
        )

    decoded_token = verify_access_token(token)

    return decoded_token["user"]
