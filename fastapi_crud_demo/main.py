from fastapi import FastAPI

from fastapi_crud_demo.routes import health

app = FastAPI()

app.include_router(health.router)
