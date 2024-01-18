from dotenv import load_dotenv
from fastapi import FastAPI

from fastapi_crud_demo.routes import health, team

load_dotenv()

app = FastAPI()

app.include_router(health.router)
app.include_router(team.router)
