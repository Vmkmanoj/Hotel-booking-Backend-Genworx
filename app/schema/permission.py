from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PermissionBase(BaseModel):
    name: str
    modules: str
    description: Optional[str] = None


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):
    name: Optional[str] = None
    modules: Optional[str] = None
    description: Optional[str] = None


class PermissionResponse(PermissionBase):
    id: UUID
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }