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
    CustomerRegisterRequest,
    LoginRequest,
    MessageResponse,
    PropertyOwnerRegisterRequest,
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
        "is_active": current_user.is_active,
    }