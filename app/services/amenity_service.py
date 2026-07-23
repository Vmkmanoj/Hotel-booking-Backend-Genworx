from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.amenity_repository import AmenityRepository
from app.schema.amenity_schema import AmenityCreate, AmenityUpdate


class AmenityService:

    @staticmethod
    async def create_amenity(
        db: AsyncSession,
        amenity_data: AmenityCreate
    ):
        existing = await AmenityRepository.get_by_name(
            db,
            amenity_data.name
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Amenity already exists."
            )

        return await AmenityRepository.create(
            db,
            amenity_data
        )

    @staticmethod
    async def get_amenity(
        db: AsyncSession,
        amenity_id: UUID
    ):
        amenity = await AmenityRepository.get_by_id(
            db,
            amenity_id
        )

        if not amenity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Amenity not found."
            )

        return amenity

    @staticmethod
    async def get_all_amenities(
        db: AsyncSession
    ):
        return await AmenityRepository.get_all(
            db
        )

    @staticmethod
    async def update_amenity(
        db: AsyncSession,
        amenity_id: UUID,
        amenity_data: AmenityUpdate
    ):
        amenity = await AmenityRepository.get_by_id(
            db,
            amenity_id
        )

        if not amenity:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Amenity not found."
            )

        return await AmenityRepository.update(
            db,
            amenity,
            amenity_data
        )

    # @staticmethod
    # async def delete_amenity(
    #     db: AsyncSession,
    #     amenity_id: UUID
    # ):
    #     amenity = await AmenityRepository.get_by_id(
    #         db,
    #         amenity_id
    #     )
    #
    #     if not amenity:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail="Amenity not found."
    #         )
    #
    #     await AmenityRepository.delete(
    #         db,
    #         amenity
    #     )
    #
    #     return {
    #         "message": "Amenity deleted successfully."
    #     }