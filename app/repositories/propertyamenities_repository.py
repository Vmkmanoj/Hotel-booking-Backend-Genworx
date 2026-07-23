from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.propertyamenities import PropertyAmenity
from app.schema.propertyamenities_schema import (
    PropertyAmenityCreate,
    PropertyAmenityUpdate,
)


class PropertyAmenityRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        property_amenity_data: PropertyAmenityCreate,
    ):
        property_amenity = PropertyAmenity(
            **property_amenity_data.model_dump()
        )

        db.add(property_amenity)

        await db.commit()
        await db.refresh(property_amenity)

        return property_amenity

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        property_amenity_id: UUID,
    ):
        result = await db.execute(
            select(PropertyAmenity).where(
                PropertyAmenity.id == property_amenity_id
            )
        )

        return result.scalars().first()

    @staticmethod
    async def get_all(
        db: AsyncSession,
    ):
        result = await db.execute(
            select(PropertyAmenity)
        )

        return result.scalars().all()

    @staticmethod
    async def update(
        db: AsyncSession,
        property_amenity: PropertyAmenity,
        property_amenity_data: PropertyAmenityUpdate,
    ):
        update_data = property_amenity_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(property_amenity, key, value)

        await db.commit()
        await db.refresh(property_amenity)

        return property_amenity

    # @staticmethod
    # async def delete(
    #     db: AsyncSession,
    #     property_amenity: PropertyAmenity,
    # ):
    #     db.delete(property_amenity)
    #     await db.commit()