from fastapi import HTTPException

from app.models.property import Property
from app.repositories.super_admin_repository import (
    SuperAdminPropertyRepository,
)

from app.schema.super_admin_schema import (
    MessageResponse,
)


class SuperAdminPropertyService:

    def __init__(self, db):

        self.db = db
        self.repo = SuperAdminPropertyRepository(db)

    def get_pending_properties(self):

        return self.repo.get_pending_properties()
    
    def get_all_approved_property(self):

        property = self.repo.get_approve_property()
         
        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )
        
        return property
         

    def get_property(self, property_id):

        property = self.repo.get_property_by_id(property_id)

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        return property

    def approve_property(self, property_id, request):

        property = (
            self.db.query(Property)
            .filter(Property.id == property_id)
            .first()
        )

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        if property.status == "APPROVED":
            raise HTTPException(
                status_code=400,
                detail="Property already approved"
            )

        self.repo.approve_property(property)

        return MessageResponse(
            success=True,
            message="Property approved successfully."
        )
    

    def reject_property(
        self,
        property_id,
        request
                ):

        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        self.repo.reject_property(
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property rejected successfully."
        )


    def suspend_property(
        self,
        property_id,
        request
    ):

        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        self.repo.suspend_property(
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property suspended successfully."
        )


    def activate_property(
        self,
        property_id,
        request
    ):

        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        self.repo.activate_property(
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property activated successfully."
        )


    def delete_property(
        self,
        property_id
    ):

        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        self.repo.delete_property(property)

        return MessageResponse(
            success=True,
            message="Property deleted successfully."
        )