from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_crud_demo.routes import health

load_dotenv()

app = FastAPI()

app.include_router(health.router)
