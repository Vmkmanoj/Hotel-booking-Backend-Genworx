# ============================================================
# Standard Library
# ============================================================

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ============================================================
# Local Imports
# ============================================================

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.users.models.roles import Role


class User(BaseModel):
    """
    Represents every authenticated user in the system.

    Roles:
    - Super Admin
    - Property Owner
    - Customer
    """

    __tablename__ = "users"

    # ========================================================
    # Authentication
    # ========================================================

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # ========================================================
    # Personal Information
    # ========================================================

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
        unique=True,
    )

    profile_image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # ========================================================
    # Account Status
    # ========================================================

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ========================================================
    # Role
    # ========================================================

    role_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "roles.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    # ========================================================
    # Relationships
    # ========================================================

    role: Mapped["Role"] = relationship(
        back_populates="users",
    )