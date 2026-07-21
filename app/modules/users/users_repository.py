# ============================================================
# Third Party
# ============================================================

from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.modules.users.models.roles import Role
from app.modules.users.models.users import User


class UsersRepository:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    # ========================================================
    # Get User By ID
    # ========================================================

    async def get_user_by_id(
        self,
        user_id: UUID,
    ) -> User | None:

        result = await self.db.execute(
            select(User).where(
                User.id == user_id,
            )
        )

        return result.scalar_one_or_none()

    # ========================================================
    # Get Role By Name
    # ========================================================

    async def get_role_by_name(
        self,
        role_name: str,
    ) -> Role | None:

        result = await self.db.execute(
            select(Role).where(
                Role.name == role_name,
            )
        )

        return result.scalar_one_or_none()

    # ========================================================
    # Get All Users
    # ========================================================

    async def get_all_users(self) -> list[User]:

        result = await self.db.execute(
            select(User).order_by(
                User.created_at.desc(),
            )
        )

        return list(result.scalars().all())

    # ========================================================
    # Count Users
    # ========================================================

    async def count_users(self) -> int:

        result = await self.db.execute(
            select(
                func.count(User.id)
            )
        )

        return result.scalar_one()

    # ========================================================
    # Save User
    # ========================================================

    async def save_user(
        self,
        user: User,
    ) -> User:

        await self.db.commit()

        await self.db.refresh(user)

        return user