from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.amenities import Amenity
from app.schema.amenity_schema import AmenityCreate, AmenityUpdate


class AmenityRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        amenity_data: AmenityCreate
    ):
        amenity = Amenity(
            **amenity_data.model_dump()
        )

        db.add(amenity)

        await db.commit()
        await db.refresh(amenity)

        return amenity

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        amenity_id: UUID
    ):
        result = await db.execute(
            select(Amenity).where(
                Amenity.id == amenity_id
            )
        )

        return result.scalars().first()

    @staticmethod
    async def get_by_name(
        db: AsyncSession,
        name: str
    ):
        result = await db.execute(
            select(Amenity).where(
                Amenity.name == name
            )
        )

        return result.scalars().first()

    @staticmethod
    async def get_all(
        db: AsyncSession
    ):
        result = await db.execute(
            select(Amenity)
        )

        return result.scalars().all()

    @staticmethod
    async def update(
        db: AsyncSession,
        amenity: Amenity,
        amenity_data: AmenityUpdate
    ):
        update_data = amenity_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(amenity, key, value)

        await db.commit()
        await db.refresh(amenity)

        return amenity

    # @staticmethod
    # async def delete(
    #     db: AsyncSession,
    #     amenity: Amenity
    # ):
    #     db.delete(amenity)
    #     await db.commit()