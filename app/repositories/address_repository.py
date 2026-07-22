from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.address import Address
from app.schema.address import AddressCreate, AddressUpdate


class AddressRepository:

    @staticmethod
<<<<<<< Updated upstream
    async def create(db: AsyncSession, address_data: AddressCreate):
=======
    async def create(
        db: AsyncSession,
        address_data: AddressCreate
    ):
>>>>>>> Stashed changes
        try:
            address = Address(**address_data.model_dump())

            db.add(address)
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
            await db.commit()
            await db.refresh(address)

            return address

        except Exception:
            await db.rollback()
            raise

    @staticmethod
<<<<<<< Updated upstream
    async def get_all(db: AsyncSession):
        try:
            return (await db.execute(select(Address))).scalars().all()

        except Exception:
            raise

    @staticmethod
    async def get_by_id(db: AsyncSession, address_id):
        try:
            return (await db.execute(
                select(Address).where(Address.id == address_id)
            )).scalar_one_or_none()
=======
    async def get_all(
        db: AsyncSession
    ):
        try:
            result = await db.execute(
                select(Address)
            )
>>>>>>> Stashed changes

            return result.scalars().all()

        except Exception:
            raise

    @staticmethod
<<<<<<< Updated upstream
    async def update(db: AsyncSession, address: Address, address_data: AddressUpdate):
=======
    async def get_by_id(
        db: AsyncSession,
        address_id
    ):
>>>>>>> Stashed changes
        try:
            result = await db.execute(
                select(Address).where(
                    Address.id == address_id
                )
            )

            return result.scalars().first()

        except Exception:
            raise

    @staticmethod
    async def update(
        db: AsyncSession,
        address: Address,
        address_data: AddressUpdate
    ):
        try:
            update_data = address_data.model_dump(
                exclude_unset=True
            )

            for key, value in update_data.items():
                setattr(address, key, value)

            await db.commit()
            await db.refresh(address)

            return address

        except Exception:
            await db.rollback()
            raise

<<<<<<< Updated upstream
    @staticmethod
    async def delete(db: AsyncSession, address: Address):
        try:
            await db.delete(address)
            await db.commit()

        except Exception:
            await db.rollback()
            raise
=======
    # @staticmethod
    # async def delete(
    #     db: AsyncSession,
    #     address: Address
    # ):
    #     try:
    #         await db.delete(address)
    #         await db.commit()
    #
    #     except Exception:
    #         await db.rollback()
    #         raise
>>>>>>> Stashed changes
