# ============================================================
# Third Party
# ============================================================

from uuid import UUID

from fastapi import (
    Depends,
    HTTPException,
    status,
)

from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from jose import JWTError

from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.core.jwt import decode_token
from app.database import get_db

from app.modules.auth.auth_repository import AuthRepository
from app.modules.users.models.users import User

# ============================================================
# HTTP Bearer Security
# ============================================================

security = HTTPBearer()

# ============================================================
# JWT Dependency
# ============================================================


async def get_current_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    """
    Extract and validate JWT.

    Returns:
        Decoded JWT payload.
    """

    token = credentials.credentials

    try:
        payload = decode_token(token)

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token.",
        )

    return payload


# ============================================================
# Current Authenticated User
# ============================================================


async def get_current_user(
    payload: dict = Depends(get_current_token),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Returns the authenticated user.

    Raises:
        401 -> User does not exist.
        403 -> User account is inactive.
    """

    user_id = payload["sub"]

    repository = AuthRepository(db)

    user = await repository.get_user_by_id(
        UUID(payload["sub"]),
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found.",
        )

    # Attach JWT payload for downstream dependencies
    user.jwt_payload = payload

    return user