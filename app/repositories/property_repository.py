from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.property import Property
from app.schema.property_schema import PropertyUpdate
from app.models.address import Address


class PropertyRepository:

    @staticmethod
    async def create(db: AsyncSession, address: Address, property_obj: Property):
        try:
            db.add(address)

            await db.flush()

            property_obj.address_id = address.id

            db.add(property_obj)

            await db.commit()

            await db.refresh(address)
            await db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            await db.rollback()
            raise

        
    @staticmethod
    async def get_all(db: AsyncSession):
        try:
            return (await db.execute(select(Property))).scalars().all()

        except SQLAlchemyError:
            raise

    @staticmethod
    async def get_by_owner_id(db: AsyncSession, owner_id: UUID):
        try:
            return (await db.execute(
                select(Property).where(Property.owner_id == owner_id)
            )).scalars().all()

        except SQLAlchemyError:
            raise

    @staticmethod
    async def get_by_id(db: AsyncSession, property_id: UUID):
        try:
            return (await db.execute(
                select(Property).where(Property.id == property_id)
            )).scalar_one_or_none()

        except SQLAlchemyError:
            raise

    @staticmethod
    async def update(
        db: AsyncSession,
        property_obj: Property,
        property_data: PropertyUpdate
    ):
        try:

            update_data = property_data.model_dump(exclude_unset=True)

            for key, value in update_data.items():
                setattr(property_obj, key, value)

            await db.commit()
            await db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            await db.rollback()
            raise

    @staticmethod
    async def archive(db: AsyncSession, property_obj: Property):
        try:

            property_obj.status = "Archived"

            await db.commit()
            await db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            await db.rollback()
            raise

    @staticmethod
    async def submit_for_review(db: AsyncSession, property_obj: Property):
        try:

            property_obj.status = "Pending Review"

            await db.commit()
            await db.refresh(property_obj)

            return property_obj

        except SQLAlchemyError:
            await db.rollback()
            raise

    @staticmethod
    async def delete(db: AsyncSession, property_obj: Property):
        try:

            await db.delete(property_obj)
            await db.commit()

            return True

        except SQLAlchemyError:
            await db.rollback()
            raise
