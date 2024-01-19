import uuid

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str
    password: str


class User(UserBase, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class UserCreate(UserBase):
    pass
