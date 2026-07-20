# ============================================================
# Standard Library
# ============================================================

from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ============================================================
# Customer Registration
# ============================================================

class CustomerRegisterRequest(BaseModel):
    """
    Request schema for customer registration.
    """

    first_name: str = Field(
        min_length=2,
        max_length=100,
    )

    last_name: str | None = Field(
        default=None,
        max_length=100,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


# ============================================================
# Property Owner Registration
# ============================================================

class PropertyOwnerRegisterRequest(BaseModel):
    """
    Request schema for property owner registration.
    """

    first_name: str = Field(
        min_length=2,
        max_length=100,
    )

    last_name: str | None = Field(
        default=None,
        max_length=100,
    )

    email: EmailStr

    phone_number: str | None = Field(
        default=None,
        max_length=20,
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )

    profile_image_url: str | None = None


# ============================================================
# Login
# ============================================================

class LoginRequest(BaseModel):
    """
    Login request.
    """

    email: EmailStr

    password: str


# ============================================================
# Authentication Response
# ============================================================

class AuthResponse(BaseModel):
    """
    Response returned after successful authentication.
    """

    access_token: str

    refresh_token: str

    token_type: str

    expires_in: int

    role: str


# ============================================================
# Generic Success Response
# ============================================================

class MessageResponse(BaseModel):
    """
    Generic success response.
    """

    message: str


# ============================================================
# Refresh Token
# ============================================================

class RefreshTokenRequest(BaseModel):
    refresh_token: str


# ============================================================
# Forgot Password
# ============================================================

class ForgotPasswordRequest(BaseModel):
    email: EmailStr


# ============================================================
# Reset Password
# ============================================================

class ResetPasswordRequest(BaseModel):
    reset_token: str

    new_password: str = Field(
        min_length=8,
        max_length=128,
    )

    confirm_password: str = Field(
        min_length=8,
        max_length=128,
    )


# ============================================================
# Change Password
# ============================================================

class ChangePasswordRequest(BaseModel):
    current_password: str

    new_password: str = Field(
        min_length=8,
        max_length=128,
    )

    confirm_password: str = Field(
        min_length=8,
        max_length=128,
    )


# ============================================================
# User Response
# ============================================================

class UserResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    first_name: str

    last_name: str | None

    email: EmailStr

    phone_number: str | None

    profile_image_url: str | None

    role: str