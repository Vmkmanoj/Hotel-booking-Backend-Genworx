from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schema.amenity_schema import (
    AmenityCreate,
    AmenityUpdate,
    AmenityResponse
)
from app.services.amenity_service import AmenityService

amenitiesRouter = APIRouter()


@amenitiesRouter.post(
    "/create",
    response_model=AmenityResponse
)
async def create_amenity(
    amenity: AmenityCreate,
    db: AsyncSession = Depends(get_db)
):
    return await AmenityService.create_amenity(
        db,
        amenity
    )


@amenitiesRouter.get(
    "/",
    response_model=list[AmenityResponse]
)
async def get_all_amenities(
    db: AsyncSession = Depends(get_db)
):
    return await AmenityService.get_all_amenities(
        db
    )


@amenitiesRouter.get(
    "/{amenity_id}",
    response_model=AmenityResponse
)
async def get_amenity(
    amenity_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await AmenityService.get_amenity(
        db,
        amenity_id
    )


@amenitiesRouter.patch(
    "/{amenity_id}",
    response_model=AmenityResponse
)
async def update_amenity(
    amenity_id: UUID,
    amenity: AmenityUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await AmenityService.update_amenity(
        db,
        amenity_id,
        amenity
    )


# @amenitiesRouter.delete(
#     "/{amenity_id}"
# )
# async def delete_amenity(
#     amenity_id: UUID,
#     db: AsyncSession = Depends(get_db)
# ):
#     return await AmenityService.delete_amenity(
#         db,
#         amenity_id
#     )