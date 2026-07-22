from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

<<<<<<< Updated upstream
from app.models.property import Property, PropertyStatus
=======
from app.models.property import Property
from app.models.address import Address
>>>>>>> Stashed changes
from app.repositories.property_repository import PropertyRepository
from app.schema.property_schema import PropertyCreate, PropertyUpdate
from app.models.address import Address


class PropertyService:

    @staticmethod
    async def create_property(
        db: AsyncSession,
        property_data: PropertyCreate
    ):

        try:

            address = Address(
                address_line_1=property_data.address_line_1,
                address_line_2=property_data.address_line_2,
                city=property_data.city,
                state=property_data.state,
                country=property_data.country,
                postal_code=property_data.postal_code,
                created_by=str(property_data.owner_id),
                updated_by=str(property_data.owner_id),
            )

            property_obj = Property(
                owner_id=property_data.owner_id,
                property_name=property_data.property_name,
                description=property_data.description,
                property_type=property_data.property_type,
                star_rating=property_data.star_rating,
                contact_email=property_data.contact_email,
                contact_number=property_data.contact_number,
                cancellation_policy=property_data.cancellation_policy,
                house_rules=property_data.house_rules,
                child_policy=property_data.child_policy,
                pet_policy=property_data.pet_policy,
                smoking_policy=property_data.smoking_policy,
                check_in_time=property_data.check_in_time,
                check_out_time=property_data.check_out_time,
<<<<<<< Updated upstream
                status=PropertyStatus.PENDING.value,
=======
                status="PENDING",
>>>>>>> Stashed changes
                is_verified=False,
                created_by=str(property_data.owner_id),
                updated_by=str(property_data.owner_id),
            )

<<<<<<< Updated upstream
            property = await PropertyRepository.create(
=======
            property_created = await PropertyRepository.create(
>>>>>>> Stashed changes
                db=db,
                address=address,
                property_obj=property_obj
            )

            return {
                "message": "Property created successfully.",
                "data": property_created
            }

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    @staticmethod
    async def get_my_properties(
        db: AsyncSession,
        owner_id: UUID
    ):
        try:

            properties = await PropertyRepository.get_by_owner_id(
                db=db,
                owner_id=owner_id
            )

            return {
                "message": "Properties fetched successfully.",
                "data": properties
            }

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch properties."
            )

    @staticmethod
    async def get_property_details(
        db: AsyncSession,
        property_id: UUID
    ):
        try:

            property_obj = await PropertyRepository.get_by_id(
                db=db,
                property_id=property_id
            )

            if property_obj is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Property not found."
                )

            return {
                "message": "Property details fetched successfully.",
                "data": property_obj
            }

        except HTTPException:
            raise

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to fetch property."
            )

    @staticmethod
    async def update_property(
        db: AsyncSession,
        property_id: UUID,
        owner_id: UUID,
        property_data: PropertyUpdate
    ):
        try:

            property_obj = await PropertyRepository.get_by_id(
                db=db,
                property_id=property_id
            )

            if property_obj is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Property not found."
                )

            if property_obj.owner_id != owner_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You are not authorized to update this property."
                )

            updated_property = await PropertyRepository.update(
                db=db,
                property_obj=property_obj,
                property_data=property_data
            )

            return {
                "message": "Property updated successfully.",
                "data": updated_property
            }

        except HTTPException:
            raise

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update property."
            )

    @staticmethod
    async def archive_property(
        db: AsyncSession,
        property_id: UUID,
        owner_id: UUID
    ):
        try:

            property_obj = await PropertyRepository.get_by_id(
                db=db,
                property_id=property_id
            )

            if property_obj is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Property not found."
                )

            if property_obj.owner_id != owner_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You are not authorized to archive this property."
                )

            archived_property = await PropertyRepository.archive(
                db=db,
                property_obj=property_obj
            )

            return {
                "message": "Property archived successfully.",
                "data": archived_property
            }

        except HTTPException:
            raise

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to archive property."
            )

    @staticmethod
    async def submit_property_for_review(
        db: AsyncSession,
        property_id: UUID,
        owner_id: UUID
    ):
        try:

            property_obj = await PropertyRepository.get_by_id(
                db=db,
                property_id=property_id
            )

            if property_obj is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Property not found."
                )

            if property_obj.owner_id != owner_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You are not authorized to submit this property."
                )

            if property_obj.status == "Archived":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Archived properties cannot be submitted for review."
                )

            submitted_property = await PropertyRepository.submit_for_review(
                db=db,
                property_obj=property_obj
            )

            return {
                "message": "Property submitted for review successfully.",
                "data": submitted_property
            }

        except HTTPException:
            raise

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to submit property for review."
<<<<<<< Updated upstream
            )

    @staticmethod
    async def delete_draft_property(
        db: AsyncSession,
        property_id: UUID,
        owner_id: UUID
    ):
        try:

            property_obj = await PropertyRepository.get_by_id(
                db=db,
                property_id=property_id
            )

            if property_obj is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Property not found."
                )

            if property_obj.owner_id != owner_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You are not authorized to delete this property."
                )

            if property_obj.status != "Draft":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Only draft properties can be deleted."
                )

            await PropertyRepository.delete(
                db=db,
                property_obj=property_obj
            )

            return {
                "message": "Property deleted successfully."
            }

        except HTTPException:
            raise

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to delete property."
            )
=======
            )
>>>>>>> Stashed changes
