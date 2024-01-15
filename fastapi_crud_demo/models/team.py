from sqlmodel import SQLModel, Field


class TeamBase(SQLModel):
    name: str
    description: str


class Team(TeamBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class TeamCreate(TeamBase):
    pass
