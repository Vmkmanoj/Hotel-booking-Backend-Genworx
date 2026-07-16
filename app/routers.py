from fastapi import APIRouter
from app.api.auth.auth import authRouter

router = APIRouter(prefix="/api/v1")

router.include_router(
    authRouter,
    prefix="/auth",
    tags=["auth"]
)

