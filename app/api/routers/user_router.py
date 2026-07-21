# ============================================================
# Third Party
# ============================================================

from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
)

from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.database import get_db

from app.dependencies.auth import (
    get_current_user,
)

from app.dependencies.authorization import require_roles

from app.modules.users.models.users import User

from app.modules.users.users_repository import UsersRepository

from app.modules.users.users_schemas import (
    CurrentUserResponse,
    UpdateProfileRequest,
    UserListResponse,
    UserResponse,
    UpdateUserRequest
)

from app.modules.users.users_service import UsersService

# ============================================================
# Router
# ============================================================

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

# ============================================================
# Dependencies
# ============================================================

def get_users_service(
    db: AsyncSession = Depends(get_db),
) -> UsersService:
    """
    Return a UsersService instance.
    """

    repository = UsersRepository(db)

    return UsersService(repository)

# ============================================================
# Self Profile
# ============================================================

@router.get(
    "/me",
    response_model=CurrentUserResponse,
)
async def get_my_profile(
    current_user: User = Depends(get_current_user),
    service: UsersService = Depends(
        get_users_service,
    ),
):
    """
    Return the authenticated user's profile.
    """

    return await service.get_my_profile(
        current_user,
    )


@router.patch(
    "/me",
    response_model=CurrentUserResponse,
)
async def update_my_profile(
    request: UpdateProfileRequest,
    current_user: User = Depends(get_current_user),
    service: UsersService = Depends(
        get_users_service,
    ),
):
    """
    Update the authenticated user's profile.
    """

    return await service.update_my_profile(
        current_user=current_user,
        request=request,
    )


# ============================================================
# User Administration
# ============================================================

@router.get(
    "",
    response_model=UserListResponse,
)
async def get_all_users(
    current_user: User = Depends(
        require_roles(
            "SUPER_ADMIN",
        ),
    ),
    service: UsersService = Depends(
        get_users_service,
    ),
):
    """
    Return all registered users.

    Access:
        SUPER_ADMIN
    """

    return await service.get_all_users()


@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
async def get_user_by_id(
    user_id: UUID,
    current_user: User = Depends(
        require_roles(
            "SUPER_ADMIN",
        ),
    ),
    service: UsersService = Depends(
        get_users_service,
    ),
):
    """
    Return a user by ID.

    Access:
        SUPER_ADMIN
    """

    return await service.get_user_by_id(
        user_id,
    )


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
)
async def update_user(
    user_id: UUID,
    request: UpdateUserRequest,
    current_user: User = Depends(
        require_roles(
            "SUPER_ADMIN",
        ),
    ),
    service: UsersService = Depends(
        get_users_service,
    ),
):
    """
    Update a user's profile.

    Access:
        SUPER_ADMIN
    """

    return await service.update_user(
        user_id=user_id,
        request=request,
    )

# ============================================================
# User Lifecycle
# ============================================================

@router.patch(
    "/{user_id}/activate",
    response_model=UserResponse,
)
async def activate_user(
    user_id: UUID,
    service: UsersService = Depends(
        get_users_service,
    ),
    current_user: User = Depends(
        require_roles(
            "SUPER_ADMIN",
        ),
    )
):
    """
    Activate a user account.

    Access:
        SUPER_ADMIN
    """

    return await service.activate_user(
        user_id=user_id,
    )

@router.patch(
    "/{user_id}/suspend",
    response_model=UserResponse,
)
async def suspend_user(
    user_id: UUID,
    service: UsersService = Depends(
        get_users_service,
    ),
    current_user: User = Depends(
        require_roles(
            "SUPER_ADMIN",
        ),
    )
):
    """
    Suspend a user account.

    Access:
        SUPER_ADMIN
    """

    return await service.suspend_user(
        user_id=user_id,
    )

@router.patch(
    "/{user_id}/deactivate",
    response_model=UserResponse,
)
async def deactivate_user(
    user_id: UUID,
    service: UsersService = Depends(
        get_users_service,
    ),
    current_user: User = Depends(
        require_roles(
            "SUPER_ADMIN",
        ),
    )
):
    """
    Deactivate a user account.

    Access:
        SUPER_ADMIN
    """

    return await service.deactivate_user(
        user_id=user_id,
    )