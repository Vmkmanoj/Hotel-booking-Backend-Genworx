from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.property import Property, PropertyStatus
from app.repositories.super_admin_repository import (
    SuperAdminPropertyRepository,
)

from app.schema.super_admin_schema import (
    MessageResponse,
)


class SuperAdminPropertyService:

    def __init__(self, db: AsyncSession):

        self.db = db
        self.repo = SuperAdminPropertyRepository(db)

    async def get_pending_properties(self):

<<<<<<< Updated upstream
        return await self.repo.get_pending_properties()
    
    async def get_all_approved_property(self):
=======
        return self.repo.get_pending_properties()
    
    def get_all_approved_property(self):

        property = self.repo.get_approve_property()
         
        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )
        
        return property
         
>>>>>>> Stashed changes

        property = await self.repo.get_approve_property()
         
        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )
        
        return property
         

    async def get_property(self, property_id):

        property = await self.repo.get_property_by_id(property_id)

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        return property

    async def approve_property(self, property_id, request):

        property = (await self.db.execute(
            select(Property).where(Property.id == property_id)
        )).scalar_one_or_none()

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        if property.status == PropertyStatus.APPROVED.value:
            raise HTTPException(
                status_code=400,
                detail="Property already approved"
            )

        await self.repo.approve_property(property)

        return MessageResponse(
            success=True,
            message="Property approved successfully."
        )
    

<<<<<<< Updated upstream
    async def reject_property(
=======
    def reject_property(
>>>>>>> Stashed changes
        self,
        property_id,
        request
                ):

<<<<<<< Updated upstream
        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()
=======
        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )
>>>>>>> Stashed changes

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

<<<<<<< Updated upstream
        await self.repo.reject_property(
=======
        self.repo.reject_property(
>>>>>>> Stashed changes
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property rejected successfully."
        )


<<<<<<< Updated upstream
    async def suspend_property(
=======
    def suspend_property(
>>>>>>> Stashed changes
        self,
        property_id,
        request
    ):

<<<<<<< Updated upstream
        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()
=======
        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )
>>>>>>> Stashed changes

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

<<<<<<< Updated upstream
        await self.repo.suspend_property(
=======
        self.repo.suspend_property(
>>>>>>> Stashed changes
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property suspended successfully."
        )


<<<<<<< Updated upstream
    async def activate_property(
=======
    def activate_property(
>>>>>>> Stashed changes
        self,
        property_id,
        request
    ):

<<<<<<< Updated upstream
        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()
=======
        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )
>>>>>>> Stashed changes

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

<<<<<<< Updated upstream
        await self.repo.activate_property(
=======
        self.repo.activate_property(
>>>>>>> Stashed changes
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property activated successfully."
        )


<<<<<<< Updated upstream
    async def delete_property(
=======
    def delete_property(
>>>>>>> Stashed changes
        self,
        property_id
    ):

<<<<<<< Updated upstream
        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()
=======
        property = (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                not Property.is_deleted
            )
            .first()
        )
>>>>>>> Stashed changes

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

<<<<<<< Updated upstream
        await self.repo.delete_property(property)
=======
        self.repo.delete_property(property)
>>>>>>> Stashed changes

        return MessageResponse(
            success=True,
            message="Property deleted successfully."
<<<<<<< Updated upstream
        )
=======
        )
>>>>>>> Stashed changes
