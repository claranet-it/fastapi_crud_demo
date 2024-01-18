from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    database_test_url: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
