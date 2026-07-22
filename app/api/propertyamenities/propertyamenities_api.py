from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schema.propertyamenities_schema import (
    PropertyAmenityCreate,
    PropertyAmenityUpdate,
    PropertyAmenityResponse,
)
from app.services.propertyamenities_service import (
    PropertyAmenityService,
)

propertyAmenitiesRouter = APIRouter()


@propertyAmenitiesRouter.post(
    "/create",
    response_model=PropertyAmenityResponse,
)
async def create_property_amenity(
    property_amenity: PropertyAmenityCreate,
    db: AsyncSession = Depends(get_db),
):
    return await PropertyAmenityService.create_property_amenity(
        db,
        property_amenity,
    )


@propertyAmenitiesRouter.get(
    "/",
    response_model=list[PropertyAmenityResponse],
)
async def get_all_property_amenities(
    db: AsyncSession = Depends(get_db),
):
    return await PropertyAmenityService.get_all_property_amenities(
        db
    )


@propertyAmenitiesRouter.get(
    "/{property_amenity_id}",
    response_model=PropertyAmenityResponse,
)
async def get_property_amenity(
    property_amenity_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await PropertyAmenityService.get_property_amenity(
        db,
        property_amenity_id,
    )


@propertyAmenitiesRouter.patch(
    "/{property_amenity_id}",
    response_model=PropertyAmenityResponse,
)
async def update_property_amenity(
    property_amenity_id: UUID,
    property_amenity: PropertyAmenityUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await PropertyAmenityService.update_property_amenity(
        db,
        property_amenity_id,
        property_amenity,
    )


# @propertyAmenitiesRouter.delete(
#     "/{property_amenity_id}",
# )
# async def delete_property_amenity(
#     property_amenity_id: UUID,
#     db: AsyncSession = Depends(get_db),
# ):
#     return await PropertyAmenityService.delete_property_amenity(
#         db,
#         property_amenity_id,
#     )