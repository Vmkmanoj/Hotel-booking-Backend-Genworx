from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PropertyImageCreate(BaseModel):
    property_id: UUID
    image_url: str
    caption: str | None = None
    is_primary: bool = False
    is_cover: bool = False
    display_order: int = 1


class PropertyImageUpdate(BaseModel):
    image_url: str | None = None
    caption: str | None = None
    is_primary: bool | None = None
    is_cover: bool | None = None
    display_order: int | None = None


class PropertyImageResponse(BaseModel):
    id: UUID
    property_id: UUID
    image_url: str
    caption: str | None = None
    is_primary: bool
    is_cover: bool
    display_order: int

    created_at: datetime
    updated_at: datetime
    created_by: str | None = None
    updated_by: str | None = None

    model_config = ConfigDict(from_attributes=True)