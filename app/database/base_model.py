# ============================================================
# Standard Library
# ============================================================

from datetime import datetime, timezone
from uuid import UUID, uuid4

# ============================================================
# Third Party
# ============================================================

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

# ============================================================
# Local Imports
# ============================================================

from app.database.base import Base


class BaseModel(Base):
    """
    Abstract base model inherited by all database tables.

    Provides:
    - UUID Primary Key
    - Audit Information
    - Created Timestamp
    - Updated Timestamp
    """

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    created_by: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        nullable=True,
    )

    updated_by: Mapped[UUID | None] = mapped_column(
        PG_UUID(as_uuid=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )