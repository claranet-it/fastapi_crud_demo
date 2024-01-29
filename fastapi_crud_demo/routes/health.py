from fastapi import APIRouter

router = APIRouter(
    prefix="/api/health",
    tags=["utils"],
)


@router.get("/")
async def root():
    return {"status": "ok"}
