# ============================================================
# Standard Library
# ============================================================

from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.modules.users.models.roles import Role
from app.modules.users.models.users import User


class AuthRepository:
    """
    Repository responsible for all authentication-related
    database operations.
    """

    def __init__(self, db: AsyncSession):
        self.db = db

    # ========================================================
    # User Operations
    # ========================================================

    async def get_user_by_email(
        self,
        email: str,
    ) -> User | None:
        """
        Fetch a user using email.
        """

        result = await self.db.execute(
            select(User).where(User.email == email)
        )

        return result.scalar_one_or_none()
    
    async def get_user_by_id(
        self,
        user_id: UUID,
    ) -> User | None:
        """
        Fetch a user by primary key.
        """

        result = await self.db.execute(
            select(User).where(
                User.id == user_id,
            )
        )

        return result.scalar_one_or_none()

    async def create_user(
        self,
        user: User,
    ) -> User:
        """
        Persist a new user.
        """

        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user

    async def update_user_password(
        self,
        user: User,
        password_hash: str,
    ) -> None:
        """
        Update user's password.
        """

        user.password_hash = password_hash

        await self.db.commit()

        await self.db.refresh(user)

    # ========================================================
    # Role Operations
    # ========================================================

    async def get_role_by_name(
        self,
        role_name: str,
    ) -> Role | None:
        """
        Fetch a role using its name.
        """

        result = await self.db.execute(
            select(Role).where(
                Role.name == role_name
            )
        )

        return result.scalar_one_or_none()

    async def get_role_by_id(
        self,
        role_id: UUID,
    ) -> Role | None:
        """
        Fetch role by primary key.
        """

        result = await self.db.execute(
            select(Role).where(
                Role.id == role_id
            )
        )

        return result.scalar_one_or_none()