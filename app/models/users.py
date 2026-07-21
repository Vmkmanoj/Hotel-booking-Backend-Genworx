import uuid
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    phone = Column(String(20))
    avatar_url = Column(String(500))

    is_active = Column(Boolean, default=True)

    last_login_at = Column(DateTime(timezone=True))

    role_id = Column(
        "roleId",
        UUID(as_uuid=True),
        ForeignKey("roles.id", ondelete="SET NULL"),
        nullable=True,
    )

    created_by = Column(String(100))
    updated_by = Column(String(100))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Properties owned by this user
    properties = relationship(
        "Property",
        foreign_keys="Property.owner_id",
        back_populates="owner"
    )

    # Properties approved by this admin
    approved_properties = relationship(
        "Property",
        foreign_keys="Property.approved_by",
        back_populates="approved_admin"
    )