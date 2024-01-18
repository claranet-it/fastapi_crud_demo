import uuid
from typing import Optional

from sqlmodel import SQLModel, Field


class TeamBase(SQLModel):
    name: str
    description: str


class Team(TeamBase, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    name: Optional[str] = None
    description: Optional[str] = None
