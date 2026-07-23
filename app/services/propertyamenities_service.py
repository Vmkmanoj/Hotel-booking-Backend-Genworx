from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.propertyamenities_repository import (
    PropertyAmenityRepository,
)
from app.schema.propertyamenities_schema import (
    PropertyAmenityCreate,
    PropertyAmenityUpdate,
)


class PropertyAmenityService:

    @staticmethod
    async def create_property_amenity(
        db: AsyncSession,
        property_amenity_data: PropertyAmenityCreate,
    ):
        return await PropertyAmenityRepository.create(
            db,
            property_amenity_data,
        )

    @staticmethod
    async def get_property_amenity(
        db: AsyncSession,
        property_amenity_id: UUID,
    ):
        property_amenity = await PropertyAmenityRepository.get_by_id(
            db,
            property_amenity_id,
        )

        if not property_amenity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Property Amenity not found.",
            )

        return property_amenity

    @staticmethod
    async def get_all_property_amenities(
        db: AsyncSession,
    ):
        return await PropertyAmenityRepository.get_all(db)

    @staticmethod
    async def update_property_amenity(
        db: AsyncSession,
        property_amenity_id: UUID,
        property_amenity_data: PropertyAmenityUpdate,
    ):
        property_amenity = await PropertyAmenityRepository.get_by_id(
            db,
            property_amenity_id,
        )

        if not property_amenity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Property Amenity not found.",
            )

        return await PropertyAmenityRepository.update(
            db,
            property_amenity,
            property_amenity_data,
        )

    # @staticmethod
    # async def delete_property_amenity(
    #     db: AsyncSession,
    #     property_amenity_id: UUID,
    # ):
    #     property_amenity = await PropertyAmenityRepository.get_by_id(
    #         db,
    #         property_amenity_id,
    #     )
    #
    #     if not property_amenity:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail="Property Amenity not found.",
    #         )
    #
    #     await PropertyAmenityRepository.delete(
    #         db,
    #         property_amenity,
    #     )
    #
    #     return {
    #         "message": "Property Amenity deleted successfully."
    #     }