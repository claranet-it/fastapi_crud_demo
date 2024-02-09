import logging

from fastapi import FastAPI

from fastapi_crud_demo.routes import health, team, user

logging.getLogger("passlib").setLevel(logging.ERROR)

app = FastAPI(
    title="FastAPI CRUD Demo",
    description="A simple CRUD demo using FastAPI",
)

app.include_router(health.router)
app.include_router(user.router)
app.include_router(team.router)
