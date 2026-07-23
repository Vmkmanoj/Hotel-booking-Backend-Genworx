from pydantic import BaseModel, EmailStr
from uuid import UUID

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    userId : UUID
    success: bool
    message: str
    access_token: str
    token_type: str
    role : str
    status : str | None