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

        return await self.repo.get_pending_properties()
    
    async def get_all_approved_property(self):

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
    

    async def reject_property(
        self,
        property_id,
        request
                ):

        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        await self.repo.reject_property(
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property rejected successfully."
        )


    async def suspend_property(
        self,
        property_id,
        request
    ):

        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        await self.repo.suspend_property(
            property,
            request.reason
        )

        return MessageResponse(
            success=True,
            message="Property suspended successfully."
        )

    async def get_suspend_property(
        self,
    ):
        result = await self.db.execute(
            select(Property)
            .where(
                Property.is_deleted.is_(False),
                Property.status == PropertyStatus.SUSPENDED.value,
            )
            .order_by(Property.updated_at.desc())
        )
        return result.scalars().all()

    async def get_reject_property(self):

        result = await self.db.execute(
                    select(Property)
                    .where(
                        Property.is_deleted.is_(False),
                        Property.status == PropertyStatus.REJECTED.value,
                    )
                    .order_by(Property.updated_at.desc())
                )
        return result.scalars().all()
        


    async def activate_property(
        self,
        property_id,
        request
    ):

        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        await self.repo.activate_property(
            property,
            request.remarks
        )

        return MessageResponse(
            success=True,
            message="Property activated successfully."
        )


    async def delete_property(
        self,
        property_id
    ):

        property = (await self.db.execute(
            select(Property).where(
                Property.id == property_id,
                Property.is_deleted.is_(False),
            )
        )).scalar_one_or_none()

        if not property:
            raise HTTPException(
                status_code=404,
                detail="Property not found"
            )

        await self.repo.delete_property(property)

        return MessageResponse(
            success=True,
            message="Property deleted successfully."
        )
