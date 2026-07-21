from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.property import Property
from app.repositories.property_repository import PropertyRepository
from app.schema.property_schema import PropertyCreate, PropertyUpdate
from app.models.address import Address


class PropertyService:

    @staticmethod
    def create_property(
        db: Session,
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
                status="PENDING",
                is_verified=False,
                created_by=str(property_data.owner_id),
                updated_by=str(property_data.owner_id),
            )

            property = PropertyRepository.create(
                db=db,
                address=address,
                property_obj=property_obj
            )

            return {
                "message": "Property created successfully.",
                "data": property
            }

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    @staticmethod
    def get_my_properties(
        db: Session,
        owner_id: UUID
    ):
        try:

            properties = PropertyRepository.get_by_owner_id(
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
    def get_property_details(
        db: Session,
        property_id: UUID
    ):
        try:

            property_obj = PropertyRepository.get_by_id(
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
    def update_property(
        db: Session,
        property_id: UUID,
        owner_id: UUID,
        property_data: PropertyUpdate
    ):
        try:

            property_obj = PropertyRepository.get_by_id(
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

            updated_property = PropertyRepository.update(
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
    def archive_property(
        db: Session,
        property_id: UUID,
        owner_id: UUID
    ):
        try:

            property_obj = PropertyRepository.get_by_id(
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

            archived_property = PropertyRepository.archive(
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
    def submit_property_for_review(
        db: Session,
        property_id: UUID,
        owner_id: UUID
    ):
        try:

            property_obj = PropertyRepository.get_by_id(
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

            # Optional Business Rule
            if property_obj.status == "Archived":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Archived properties cannot be submitted for review."
                )

            submitted_property = PropertyRepository.submit_for_review(
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
            )

    @staticmethod
    def delete_draft_property(
        db: Session,
        property_id: UUID,
        owner_id: UUID
    ):
        try:

            property_obj = PropertyRepository.get_by_id(
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

            PropertyRepository.delete(
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