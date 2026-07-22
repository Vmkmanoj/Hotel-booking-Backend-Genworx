
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import User
from app.models.roles import Role

class AuthRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_user_by_email(self, email: str):
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    async def get_user_role(self, role_id):
        result = await self.db.execute(select(Role).where(Role.id == role_id))
        return result.scalar_one_or_none()
    

    async def get_role_by_name(self, role_name: str):
        result = await self.db.execute(select(Role).where(Role.name == role_name))
        return result.scalar_one_or_none()

