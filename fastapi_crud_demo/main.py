from dotenv import load_dotenv
from fastapi import FastAPI
from routes import team

from fastapi_crud_demo.routes import health

load_dotenv()

app = FastAPI()

app.include_router(health.router)
app.include_router(team.router)
