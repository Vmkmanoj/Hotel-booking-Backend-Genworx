# ============================================================
# Standard Library
# ============================================================

from datetime import time, datetime

from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import (
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    Time,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

# ============================================================
# Local Imports
# ============================================================

from app.database.base_model import BaseModel

from app.modules.properties.property_enums import (
    PropertyStatus,
    PropertyType,
    VerificationStatus,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.users.models.users import User

# ============================================================
# Property Model
# ============================================================

class Property(BaseModel):
    """
    Represents a rental property listed on the platform.
    """

    __tablename__ = "properties"

    # ============================================================
    # Ownership
    # ============================================================

    owner_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )


    # ============================================================
    # Basic Information
    # ============================================================

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    property_type: Mapped[PropertyType] = mapped_column(
        Enum(
            PropertyType,
            name="property_type_enum",
        ),
        nullable=False,
        index=True,
    )

    # ============================================================
    # Contact Information
    # ============================================================

    contact_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    contact_phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )


    # ============================================================
    # Business Information
    # ============================================================

    check_in_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    check_out_time: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )

    # ============================================================
    # Property Status
    # ============================================================

    property_status: Mapped[PropertyStatus] = mapped_column(
        Enum(
            PropertyStatus,
            name="property_status_enum",
        ),
        nullable=False,
        default=PropertyStatus.DRAFT,
        index=True,
    )

    verification_status: Mapped[
        VerificationStatus
    ] = mapped_column(
        Enum(
            VerificationStatus,
            name="verification_status_enum",
        ),
        nullable=False,
        default=VerificationStatus.PENDING,
        index=True,
    )

    # ============================================================
    # Analytics
    # ============================================================

    average_rating: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.0,
    )

    total_reviews: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    # ============================================================
    # Verification Information
    # ============================================================

    verified_by: Mapped[UUID | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )

    verified_at: Mapped[datetime | None] = mapped_column(
        nullable=True,
    )

    # ============================================================
    # Relationships
    # ============================================================

    owner: Mapped["User"] = relationship(
        foreign_keys=[owner_id],
    )

    verified_by_user: Mapped["User | None"] = relationship(
        foreign_keys=[verified_by],
    )