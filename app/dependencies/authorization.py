# ============================================================
# Third Party
# ============================================================

from fastapi import (
    Depends,
    HTTPException,
    status,
)

# ============================================================
# Local Imports
# ============================================================

from app.dependencies.auth import get_current_user

from app.modules.users.models.users import User


def require_roles(
    *allowed_roles: str,
):
    """
    Dependency that allows access only to users
    having one of the specified roles.
    """

    async def dependency(
        current_user: User = Depends(
            get_current_user,
        ),
    ) -> User:

        user_role = current_user.jwt_payload["role"]

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action.",
            )

        return current_user

    return dependency