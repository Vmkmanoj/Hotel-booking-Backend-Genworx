from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.propertyimages_repository import (
    PropertyImageRepository,
)
from app.schema.propertyimages_schema import (
    PropertyImageCreate,
    PropertyImageUpdate,
)


class PropertyImageService:

    @staticmethod
    async def create_property_image(
        db: AsyncSession,
        property_image_data: PropertyImageCreate,
    ):
        return await PropertyImageRepository.create(
            db,
            property_image_data,
        )

    @staticmethod
    async def get_property_image(
        db: AsyncSession,
        image_id: UUID,
    ):
        property_image = await PropertyImageRepository.get_by_id(
            db,
            image_id,
        )

        if not property_image:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Property image not found.",
            )

        return property_image

    @staticmethod
    async def get_all_property_images(
        db: AsyncSession,
    ):
        return await PropertyImageRepository.get_all(db)

    @staticmethod
    async def update_property_image(
        db: AsyncSession,
        image_id: UUID,
        property_image_data: PropertyImageUpdate,
    ):
        property_image = await PropertyImageRepository.get_by_id(
            db,
            image_id,
        )

        if not property_image:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Property image not found.",
            )

        return await PropertyImageRepository.update(
            db,
            property_image,
            property_image_data,
        )

    # @staticmethod
    # async def delete_property_image(
    #     db: AsyncSession,
    #     image_id: UUID,
    # ):
    #     property_image = await PropertyImageRepository.get_by_id(
    #         db,
    #         image_id,
    #     )
    #
    #     if not property_image:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail="Property image not found.",
    #         )
    #
    #     await PropertyImageRepository.delete(
    #         db,
    #         property_image,
    #     )
    #
    #     return {
    #         "message": "Property image deleted successfully."
    #     }