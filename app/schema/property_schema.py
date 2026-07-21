from uuid import UUID
from decimal import Decimal
from datetime import datetime, time

from pydantic import BaseModel, EmailStr, ConfigDict

from app.models.property import PropertyStatus


class PropertyBase(BaseModel):
    property_name: str
    description: str | None = None
    property_type: str
    star_rating: int | None = None

    contact_email: EmailStr
    contact_number: str

    cancellation_policy: str | None = None
    house_rules: dict | None = None

    child_policy: str | None = None
    pet_policy: str | None = None
    smoking_policy: str | None = None

    status: PropertyStatus = PropertyStatus.PENDING

    check_in_time: time
    check_out_time: time


class PropertyCreate(PropertyBase):
    owner_id: UUID 
    address_id: UUID 


class PropertyUpdate(BaseModel):
    property_name: str | None = None
    description: str | None = None

    property_type: str | None = None
    star_rating: int | None = None

    contact_email: EmailStr | None = None
    contact_number: str | None = None

    cancellation_policy: str | None = None
    house_rules: dict | None = None

    child_policy: str | None = None
    pet_policy: str | None = None
    smoking_policy: str | None = None

    status: PropertyStatus | None = None

    check_in_time: time | None = None
    check_out_time: time | None = None


class PropertyResponse(PropertyBase):
    id: UUID

    owner_id: UUID
    address_id: UUID

    approved_by: UUID | None = None
    approval_remarks: str | None = None
    approved_at: datetime | None = None

    is_verified: bool
    is_deleted: bool

    avg_rating: Decimal | None = None
    total_reviews: int

    created_at: datetime
    updated_at: datetime

    created_by: str | None = None
    updated_by: str | None = None

    model_config = ConfigDict(from_attributes=True)