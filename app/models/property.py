import uuid
import enum

from sqlalchemy import Column,String,Boolean,DateTime, Time, Text, ForeignKey, DECIMAL, Integer, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class PropertyStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    SUSPENDED = "SUSPENDED"


class Property(Base):
    __tablename__ = "properties"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    owner_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    address_id = Column(
        UUID(as_uuid=True),
        ForeignKey("addresses.id", ondelete="CASCADE"),
        nullable=False
    )

    approved_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    property_name = Column(String(255), nullable=False)

    description = Column(Text)

    property_type = Column(String(100), nullable=False)

    star_rating = Column(Integer)

    contact_email = Column(String(255), nullable=False)

    contact_number = Column(String(20), nullable=False)

    cancellation_policy = Column(Text)

    house_rules = Column(JSONB)

    child_policy = Column(Text)

    pet_policy = Column(Text)

    smoking_policy = Column(Text)

    # The existing database migration defines this column as VARCHAR(100).
    # Keep the model aligned with that schema; PropertyStatus is still used for
    # validation at the application/schema layer.
    status = Column(
        String(100),
        nullable=False,
        default=PropertyStatus.PENDING.value,
    )

    is_verified = Column(
        Boolean,
        default=False,
        nullable=False
    )

    avg_rating = Column(
        DECIMAL(2, 1),
        default=0
    )

    total_reviews = Column(
        Integer,
        default=0,
        nullable=False
    )

    check_in_time = Column(Time, nullable=False)

    check_out_time = Column(Time, nullable=False)

    approval_remarks = Column(Text)

    approved_at = Column(DateTime)

    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    created_by = Column(String(100))

    updated_by = Column(String(100))

    # -----------------------
    # Relationships
    # -----------------------

    owner = relationship(
        "User",
        foreign_keys=[owner_id],
        back_populates="properties"
    )

    approved_admin = relationship(
        "User",
        foreign_keys=[approved_by],
        back_populates="approved_properties"
    )

    address = relationship(
        "Address",
        back_populates="property",
        uselist=False
    )

    favorites = relationship(
    "Favorite",
    back_populates="property",
    cascade="all, delete-orphan"
    )

    # rooms = relationship(
    #     "Room",
    #     back_populates="property",
    #     cascade="all, delete-orphan"
    # )

    # amenities = relationship(
    #     "PropertyAmenity",
    #     back_populates="property",
    #     cascade="all, delete-orphan"
    # )

    # images = relationship(
    #     "PropertyImage",
    #     back_populates="property",
    #     cascade="all, delete-orphan"
    # )

    # reviews = relationship(
    #     "Review",
    #     back_populates="property",
    #     cascade="all, delete-orphan"
    # )

    # bookings = relationship(
    #     "Booking",
    #     back_populates="property"
    # )
