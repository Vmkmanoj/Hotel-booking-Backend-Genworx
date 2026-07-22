import uuid
from sqlalchemy import Column, String, DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base

class PropertyAmenity(Base):
    __tablename__ = "property_amenities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.id"), nullable=False)
    amenity_id = Column(UUID(as_uuid=True), ForeignKey("amenities.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now(),nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(),nullable=False)
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)