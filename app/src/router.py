from fastapi import APIRouter
from app.src.views import user
from app.src.views import login
from app.src.views import conversion

router = APIRouter()

router.include_router(user.router, prefix="/user", tags=["user"])
router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(conversion.router, prefix="/conversion", tags=["conversion"])


@router.get("/health")
async def health():
    return {"status": "ok"}
