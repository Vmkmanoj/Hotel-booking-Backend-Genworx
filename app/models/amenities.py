import uuid
from sqlalchemy import Column, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base



class Amenity(Base):
    __tablename__ = "amenities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(150), nullable=False)
    wifi = Column(Boolean, nullable=False, default=False)
    swimming_pool = Column(Boolean, nullable=False, default=False)
    air_conditioner = Column(Boolean, nullable=False, default=False)
    spa = Column(Boolean, nullable=False, default=False)
    food_service = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)

