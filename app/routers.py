from fastapi import APIRouter
from app.api.auth.auth import authRouter
from app.api.dashborad.superAdmindashboard import dashboardRouter
from app.api.super_admin.super_admin import superAdmin
from app.api.property.property_api import propertyRouter

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



