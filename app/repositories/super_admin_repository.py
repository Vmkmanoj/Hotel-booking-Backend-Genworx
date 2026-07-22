from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.property import Property, PropertyStatus
from app.models.users import User
from app.models.address import Address
from datetime import datetime


class SuperAdminPropertyRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_pending_properties(self):

        result = await self.db.execute(
            select(
                Property.id,
                Property.property_name,
                User.first_name.label("owner_name"),
                User.email.label("owner_email"),
                Address.city,
                Address.state,
                Property.status,
                Property.created_at,
            )
            .join(User, Property.owner_id == User.id)
            .join(Address, Property.address_id == Address.id)
            .where(Property.status == PropertyStatus.PENDING.value)
            .order_by(Property.created_at.desc())
        )
        return result.all()

    async def get_property_by_id(self, property_id):

        result = await self.db.execute(
            select(
                Property.id,
                Property.property_name,
                Property.description,

                User.first_name.label("owner_name"),
                User.email.label("owner_email"),
                User.phone.label("owner_phone"),

                Address.address_line_1,
                Address.address_line_2,
                Address.city,
                Address.state,
                Address.country,
                Address.postal_code,

                Property.property_type,
                Property.status,
                Property.is_verified,
                Property.created_at,
            )
            .join(User, Property.owner_id == User.id)
            .join(Address, Property.address_id == Address.id)
            .where(Property.id == property_id)
        )
        return result.first()

    async def approve_property(self, property):

        property.status = PropertyStatus.APPROVED.value
        property.is_verified = True

        await self.db.commit()
        await self.db.refresh(property)

        return property
    
    async def get_approve_property(self):
        result = await self.db.execute(
            select(Property).where(Property.status == PropertyStatus.APPROVED.value)
        )
        return result.scalars().all()
    

    async def reject_property(
        self,
        property,
        remarks,
        admin_id=None
    ):

        property.status = PropertyStatus.REJECTED.value
        property.is_verified = False
        property.approval_remarks = remarks
        property.approved_by = admin_id
        property.approved_at = datetime.utcnow()

        await self.db.commit()
        await self.db.refresh(property)

        return property


    async def suspend_property(
        self,
        property,
        remarks,
        admin_id=None
    ):

        property.status = PropertyStatus.SUSPENDED.value
        property.approval_remarks = remarks
        property.approved_by = admin_id

        await self.db.commit()
        await self.db.refresh(property)

        return property


    async def activate_property(
        self,
        property,
        remarks,
        admin_id=None
    ):

        property.status = PropertyStatus.APPROVED.value
        property.is_verified = True
        property.approval_remarks = remarks
        property.approved_by = admin_id

        await self.db.commit()
        await self.db.refresh(property)

        return property


    async def delete_property(self, property):

        property.is_deleted = True

        await self.db.commit()
