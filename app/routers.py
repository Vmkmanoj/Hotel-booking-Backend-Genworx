from fastapi import APIRouter
from app.api.auth.auth import authRouter
from app.api.dashborad.super_admindashboard import dashboardRouter
from app.api.super_admin.super_admin import superAdmin
from app.api.property.property_api import propertyRouter
from app.api.favorite.favorite import favoriteRouter
from app.api.amenities.amenities_api import amenitiesRouter
from app.api.propertyamenities.propertyamenities_api import propertyAmenitiesRouter
from app.api.propertyimages.propertyimages_api import propertyImagesRouter
from app.api.address.address_api import addressRouter

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
    addressRouter,
    prefix="/address",
    tags=["Address"]
)

router.include_router(
    favoriteRouter,
    prefix="/favorite",
    tags=["favoriteRouter"]
)

router.include_router(
    amenitiesRouter,
    prefix="/amenity",
    tags=["Amenity"]
)

router.include_router(
    propertyAmenitiesRouter,
    prefix="/property-amenity",
    tags=["Property-Amenity"]
)
router.include_router(
    propertyImagesRouter,
    prefix="/property-image",
    tags=["Property-Image"]
)





