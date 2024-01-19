from fastapi import FastAPI

from fastapi_crud_demo.routes import health, team

app = FastAPI()

app.include_router(health.router)
app.include_router(team.router)
