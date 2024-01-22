from sqlmodel import SQLModel


class ErrorResponse(SQLModel):
    detail: str
