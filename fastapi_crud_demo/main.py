from fastapi import FastAPI

from fastapi_crud_demo.routes import health, user, team

app = FastAPI()

app.include_router(health.router)
app.include_router(user.router)
app.include_router(team.router)
