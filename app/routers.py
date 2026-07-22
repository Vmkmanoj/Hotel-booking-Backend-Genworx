from fastapi import APIRouter
from app.api.auth.auth import authRouter
from app.api.dashborad.super_admindashboard import dashboardRouter
from app.api.super_admin.super_admin import superAdmin
from app.api.property.property_api import propertyRouter
from app.api.favorite.favorite import favoriteRouter

router = APIRouter(prefix="/api/v1")

router.include_router(
    authRouter,
    prefix="/auth",
    tags=["auth"]
)

router.include_router(
    dashboardRouter,
    prefix="/super-admin-dashboard",
    tags=["Super Admin Dashboard"]
)

router.include_router(
    superAdmin,
    prefix="/super-admin",
    tags=["Super Admin"]
)

router.include_router(
    propertyRouter,
    prefix="/property",
    tags=["property"]
)

router.include_router(
    favoriteRouter,
    prefix="/favorite",
    tags=["favoriteRouter"]
)



