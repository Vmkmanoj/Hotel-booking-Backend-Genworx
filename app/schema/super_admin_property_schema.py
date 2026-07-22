from pydantic import BaseModel
from typing import Optional


class RejectPropertyRequest(BaseModel):
    reason: str


class SuspendPropertyRequest(BaseModel):
    reason: str


class ActivatePropertyRequest(BaseModel):
    reason: Optional[str] = None