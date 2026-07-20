# ============================================================
# Standard Library
# ============================================================

from typing import TYPE_CHECKING
from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ============================================================
# Local Imports
# ============================================================

from app.database.base_model import BaseModel

if TYPE_CHECKING:
    from app.modules.users.models.roles import Role
    from app.modules.users.models.permissions import Permission


class RolePermission(BaseModel):
    """
    Junction table that maps Roles to Permissions.

    A Role can have multiple Permissions.
    A Permission can belong to multiple Roles.
    """

    __tablename__ = "role_permissions"

    __table_args__ = (
        UniqueConstraint(
            "role_id",
            "permission_id",
            name="uq_role_permission",
        ),
    )

    role_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "roles.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    permission_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "permissions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ========================================================
    # Relationships
    # ========================================================

    role: Mapped["Role"] = relationship(
        back_populates="role_permissions",
    )

    permission: Mapped["Permission"] = relationship(
        back_populates="role_permissions",
    )