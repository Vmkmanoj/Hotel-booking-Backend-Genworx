from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import User
from app.models.roles import Role
from app.models.property import Property, PropertyStatus


class DashboardRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def total_users(self):
        return await self._count(select(User))

    async def total_customers(self):
        return await self._count(select(User).join(Role).where(Role.name == "CUSTOMER"))

    async def total_property_owners(self):
        return await self._count(select(User).join(Role).where(Role.name == "PROPERTY_OWNER"))

    async def total_admins(self):
        return await self._count(select(User).join(Role).where(Role.name == "SUPER_ADMIN"))

    async def total_properties(self):
        return await self._count(select(Property))

    async def pending_properties(self):
        return await self._count(select(Property).where(Property.status == PropertyStatus.PENDING.value))

    async def approved_properties(self):
        return await self._count(select(Property).where(Property.status == PropertyStatus.APPROVED.value))

    async def rejected_properties(self):
        return await self._count(select(Property).where(Property.status == PropertyStatus.REJECTED.value))

    async def suspend_properties(self):
        return await self._count(select(Property).where(Property.status == PropertyStatus.SUSPENDED.value))


    async def _count(self, statement):
        result = await self.db.execute(
            select(func.count()).select_from(statement.subquery())
        )
        return result.scalar_one()
