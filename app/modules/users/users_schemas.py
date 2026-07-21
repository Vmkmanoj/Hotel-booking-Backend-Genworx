# ============================================================
# Third Party
# ============================================================

from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from app.common.enums.user_status import UserStatus

# ============================================================
# User Profile Response
# ============================================================

class UserResponse(BaseModel):
    """
    User information returned by the API.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    first_name: str

    last_name: str | None

    email: EmailStr

    phone_number: str | None

    profile_image_url: str | None

    role_id: UUID

    user_status: UserStatus


# ============================================================
# Current User Response
# ============================================================

class CurrentUserResponse(UserResponse):
    """
    Response returned by
    GET /api/users/me
    """

    pass


# ============================================================
# Update Profile Request
# ============================================================

class UpdateProfileRequest(BaseModel):
    """
    Logged-in user profile update.
    """

    first_name: str | None = None

    last_name: str | None = None

    phone_number: str | None = None

    profile_image_url: str | None = None


# ============================================================
# Admin Update User Request
# ============================================================

class UpdateUserRequest(BaseModel):
    """
    Super Admin updates another user.
    """

    first_name: str | None = None

    last_name: str | None = None

    phone_number: str | None = None

    profile_image_url: str | None = None

    user_status: UserStatus | None = None


# ============================================================
# Change Role Request
# ============================================================

class ChangeUserRoleRequest(BaseModel):
    """
    Assign a new role.
    """

    role_name: str


# ============================================================
# User List Response
# ============================================================

class UserListResponse(BaseModel):
    """
    Response returned when
    listing users.
    """

    users: list[UserResponse]

    total: int


# ============================================================
# Common Message Response
# ============================================================

class UserMessageResponse(BaseModel):
    """
    Generic success response.
    """

    message: str