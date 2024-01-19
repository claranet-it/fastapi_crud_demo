from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    database_url: str
    database_test_url: str

    jwt_secret: Optional[str] = None

    session_auto_commit: bool = False
    session_auto_flush: bool = False

    class ConfigDict:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
