from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


# -----------------------------
# Create Schema
# -----------------------------
class AmenityCreate(BaseModel):
    name: str
    description: str | None = None
    category: str

    wifi: bool = False
    swimming_pool: bool = False
    air_conditioner: bool = False
    spa: bool = False
    food_service: bool = False


# -----------------------------
# Update Schema
# -----------------------------
class AmenityUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    category: str | None = None

    wifi: bool | None = None
    swimming_pool: bool | None = None
    air_conditioner: bool | None = None
    spa: bool | None = None
    food_service: bool | None = None


# -----------------------------
# Response Schema
# -----------------------------
class AmenityResponse(BaseModel):
    id: UUID
    name: str
    description: str | None = None
    category: str

    wifi: bool
    swimming_pool: bool
    air_conditioner: bool
    spa: bool
    food_service: bool

    created_at: datetime
    updated_at: datetime
    created_by: str | None = None
    updated_by: str | None = None

    model_config = ConfigDict(from_attributes=True)