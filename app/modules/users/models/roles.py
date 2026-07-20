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
    from app.modules.users.models.users import User


class Role(BaseModel):
    """
    Represents a system role used for Role-Based Access Control (RBAC).

    Examples:
    - SUPER_ADMIN
    - PROPERTY_OWNER
    - CUSTOMER
    """

    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
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

    users: Mapped[list["User"]] = relationship(
        back_populates="role",
    )

    role_permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan",
    )