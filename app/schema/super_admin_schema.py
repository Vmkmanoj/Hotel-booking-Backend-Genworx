from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PendingPropertyResponse(BaseModel):
    id: UUID
    property_name: str
    owner_name: str
    owner_email: str
    city: str
    state: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class PropertyDetailResponse(BaseModel):
    id: UUID
    property_name: str
    description: Optional[str]

    owner_name: str
    owner_email: str
    owner_phone: str

    address_line_1: str
    address_line_2: Optional[str]
    city: str
    state: str
    country: str
    postal_code: str

    property_type: str
    status: str
    is_verified: bool

    created_at: datetime

    class Config:
        from_attributes = True


class ApprovePropertyRequest(BaseModel):
    remarks: Optional[str] = None


class MessageResponse(BaseModel):
    success: bool
    message: str