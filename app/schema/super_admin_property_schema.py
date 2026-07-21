from pydantic import BaseModel
from typing import Optional


class RejectPropertyRequest(BaseModel):
    remarks: str


class SuspendPropertyRequest(BaseModel):
    remarks: str


class ActivatePropertyRequest(BaseModel):
    remarks: Optional[str] = None