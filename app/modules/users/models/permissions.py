# ============================================================
# Standard Library
# ============================================================

from typing import TYPE_CHECKING

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ============================================================
# Local Imports
# ============================================================

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.users.models.role_permissions import RolePermission


class Permission(BaseModel):
    """
    Represents a permission that can be assigned to one or more roles.

    Examples:
    - CREATE_PROPERTY
    - UPDATE_PROPERTY
    - DELETE_PROPERTY
    - VIEW_BOOKINGS
    """

    __tablename__ = "permissions"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    module: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    # ========================================================
    # Relationships
    # ========================================================

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="permission",
        cascade="all, delete-orphan",
    )