from fastapi import APIRouter

from app.api.routers.auth_router import router as auth_router
from app.api.routers.user_router import router as user_router
from app.api.booking_router.booking_router import router as booking_router
from app.api.payment_router.payment_router import router as payment_router


api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(user_router)
api_router.include_router(
    booking_router,
)
api_router.include_router(payment_router)