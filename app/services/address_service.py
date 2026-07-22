from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.address_repository import AddressRepository
from app.schema.address import AddressCreate, AddressUpdate


class AddressService:

    @staticmethod
    async def create_address(
        db: AsyncSession,
        address_data: AddressCreate
    ):
        try:
            return await AddressRepository.create(
                db,
                address_data
            )

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    @staticmethod
    async def get_all_addresses(
        db: AsyncSession
    ):
        try:
            return await AddressRepository.get_all(db)

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    @staticmethod
    async def get_address(
        db: AsyncSession,
        address_id: UUID
    ):
        try:
            address = await AddressRepository.get_by_id(
                db,
                address_id
            )

            if not address:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Address not found"
                )

            return address

        except HTTPException:
            raise

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    @staticmethod
    async def update_address(
        db: AsyncSession,
        address_id: UUID,
        address_data: AddressUpdate
    ):
        try:
            address = await AddressRepository.get_by_id(
                db,
                address_id
            )

            if not address:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Address not found"
                )

            return await AddressRepository.update(
                db,
                address,
                address_data
            )

        except HTTPException:
            raise

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    # @staticmethod
    # async def delete_address(
    #     db: AsyncSession,
    #     address_id: UUID
    # ):
    #     try:
    #         address = await AddressRepository.get_by_id(
    #             db,
    #             address_id
    #         )
    #
    #         if not address:
    #             raise HTTPException(
    #                 status_code=status.HTTP_404_NOT_FOUND,
    #                 detail="Address not found"
    #             )
    #
    #         await AddressRepository.delete(
    #             db,
    #             address
    #         )
    #
    #         return {
    #             "message": "Address deleted successfully"
    #         }
    #
    #     except HTTPException:
    #         raise
    #
    #     except Exception as e:
    #         raise HTTPException(
    #             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #             detail=str(e)
    #         )