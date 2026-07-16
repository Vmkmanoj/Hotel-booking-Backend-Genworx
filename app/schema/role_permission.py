from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RolePermissionBase(BaseModel):
    role_id: UUID
    permission_id: UUID


class RolePermissionCreate(RolePermissionBase):
    pass


class RolePermissionResponse(RolePermissionBase):
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }