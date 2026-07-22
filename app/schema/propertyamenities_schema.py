from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


# -----------------------------
# Create Schema
# -----------------------------
class PropertyAmenityCreate(BaseModel):
    property_id: UUID
    amenity_id: UUID


# -----------------------------
# Update Schema
# -----------------------------
class PropertyAmenityUpdate(BaseModel):
    property_id: UUID | None = None
    amenity_id: UUID | None = None


# -----------------------------
# Response Schema
# -----------------------------
class PropertyAmenityResponse(BaseModel):
    id: UUID
    property_id: UUID
    amenity_id: UUID

    created_at: datetime
    updated_at: datetime
    created_by: str | None = None
    updated_by: str | None = None

    model_config = ConfigDict(from_attributes=True)