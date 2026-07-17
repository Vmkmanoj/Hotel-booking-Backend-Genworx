from pydantic import BaseModel, EmailStr
from typing import Optional


class CustomerRegister(BaseModel):
    userName: str
    email: EmailStr
    password: str


class PropertyRegister(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    password: str
    avatar_url: Optional[str] = None


class RegisterResponse(BaseModel):
    success: bool
    message: str