from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schema.propertyimages_schema import (
    PropertyImageCreate,
    PropertyImageUpdate,
    PropertyImageResponse,
)
from app.services.propertyimages_service import (
    PropertyImageService,
)

propertyImagesRouter = APIRouter()


@propertyImagesRouter.post(
    "/create",
    response_model=PropertyImageResponse,
)
async def create_property_image(
    property_image: PropertyImageCreate,
    db: AsyncSession = Depends(get_db),
):
    return await PropertyImageService.create_property_image(
        db,
        property_image,
    )


@propertyImagesRouter.get(
    "/",
    response_model=list[PropertyImageResponse],
)
async def get_all_property_images(
    db: AsyncSession = Depends(get_db),
):
    return await PropertyImageService.get_all_property_images(
        db,
    )


@propertyImagesRouter.get(
    "/{image_id}",
    response_model=PropertyImageResponse,
)
async def get_property_image(
    image_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await PropertyImageService.get_property_image(
        db,
        image_id,
    )


@propertyImagesRouter.patch(
    "/{image_id}",
    response_model=PropertyImageResponse,
)
async def update_property_image(
    image_id: UUID,
    property_image: PropertyImageUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await PropertyImageService.update_property_image(
        db,
        image_id,
        property_image,
    )


# @propertyImagesRouter.delete(
#     "/{image_id}",
# )
# async def delete_property_image(
#     image_id: UUID,
#     db: AsyncSession = Depends(get_db),
# ):
#     return await PropertyImageService.delete_property_image(
#         db,
#         image_id,
#     )