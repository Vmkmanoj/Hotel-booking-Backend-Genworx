# ============================================================
# Third Party
# ============================================================

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.modules.users.models.users import User

from app.modules.auth.auth_schemas import (
    AuthResponse,
    ChangePasswordRequest,
    CustomerRegisterRequest,
    LoginRequest,
    MessageResponse,
    PropertyOwnerRegisterRequest,
    RefreshTokenRequest,
)

from app.modules.auth.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


# ============================================================
# Customer Registration
# ============================================================

@router.post(
    "/register/customer",
    response_model=MessageResponse,
    status_code=201,
)
async def register_customer(
    request: CustomerRegisterRequest,
    db: AsyncSession = Depends(get_db),
):

    service = AuthService(db)

    return await service.register_customer(request)


# ============================================================
# Property Owner Registration
# ============================================================

@router.post(
    "/register/owner",
    response_model=MessageResponse,
    status_code=201,
)
async def register_property_owner(
    request: PropertyOwnerRegisterRequest,
    db: AsyncSession = Depends(get_db),
):

    service = AuthService(db)

    return await service.register_property_owner(request)


# ============================================================
# Login
# ============================================================

@router.post(
    "/login",
    response_model=AuthResponse,
)
async def login(
    request: LoginRequest,
    db: AsyncSession = Depends(get_db),
):

    service = AuthService(db)

    return await service.login(
        email=request.email,
        password=request.password,
    )


# ============================================================
# Current User
# ============================================================

@router.get(
    "/me",
)
async def get_me(
    current_user: User = Depends(get_current_user),
):
    """
    Returns the currently authenticated user.
    """

    return {
        "id": str(current_user.id),
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email,
        "role_id": str(current_user.role_id),
        "user_status": current_user.user_status,
    }



# ============================================================
# Refresh Access Token
# ============================================================

@router.post(
    "/refresh-token",
    response_model=AuthResponse,
)
async def refresh_access_token(
    request: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db),
):
    """
    Generate a new access token
    using a valid refresh token.
    """

    service = AuthService(db)

    return await service.refresh_access_token(
        request.refresh_token,
    )


# ============================================================
# Change Password
# ============================================================

@router.post(
    "/change-password",
    response_model=MessageResponse,
)
async def change_password(
    request: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Change the password of the authenticated user.
    """

    service = AuthService(db)

    return await service.change_password(
        current_user=current_user,
        current_password=request.current_password,
        new_password=request.new_password,
    )

# ============================================================
# Logout
# ============================================================

@router.post(
    "/logout",
    response_model=MessageResponse,
)
async def logout(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Logout the authenticated user.

    Since JWT authentication is stateless,
    the backend simply validates the user
    and returns a success response.
    """

    service = AuthService(db)

    return await service.logout()