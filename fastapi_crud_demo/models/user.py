import uuid

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str


class UserWithPassword(UserBase):
    password: str


class User(UserWithPassword, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class UserCreate(UserWithPassword):
    pass


class UserLogin(UserWithPassword):
    pass


class CurrentUser(UserBase):
    id: str
