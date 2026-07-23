from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.propertyimages import PropertyImage
from app.schema.propertyimages_schema import (
    PropertyImageCreate,
    PropertyImageUpdate,
)


class PropertyImageRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        property_image_data: PropertyImageCreate,
    ):
        property_image = PropertyImage(
            **property_image_data.model_dump()
        )

        db.add(property_image)

        await db.commit()
        await db.refresh(property_image)

        return property_image

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        image_id: UUID,
    ):
        result = await db.execute(
            select(PropertyImage).where(
                PropertyImage.id == image_id
            )
        )

        return result.scalars().first()

    @staticmethod
    async def get_all(
        db: AsyncSession,
    ):
        result = await db.execute(
            select(PropertyImage)
        )

        return result.scalars().all()

    @staticmethod
    async def update(
        db: AsyncSession,
        property_image: PropertyImage,
        property_image_data: PropertyImageUpdate,
    ):
        update_data = property_image_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(property_image, key, value)

        await db.commit()
        await db.refresh(property_image)

        return property_image

    # @staticmethod
    # async def delete(
    #     db: AsyncSession,
    #     property_image: PropertyImage,
    # ):
    #     db.delete(property_image)
    #     await db.commit()