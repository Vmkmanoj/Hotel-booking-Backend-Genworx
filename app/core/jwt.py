# ============================================================
# Standard Library
# ============================================================

from datetime import datetime, timedelta, timezone
from uuid import UUID

# ============================================================
# Third Party
# ============================================================

from jose import JWTError, jwt

# ============================================================
# Local Imports
# ============================================================

from app.core.config import settings

# ============================================================
# Constants
# ============================================================

ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"

# ============================================================
# Public Functions
# ============================================================


def create_access_token(
    user_id: UUID,
    role: str,
) -> str:
    """
    Create a JWT Access Token.

    Args:
        user_id: Authenticated user's UUID.
        role: User's role.

    Returns:
        Encoded JWT access token.
    """

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "role": role,
        "type": ACCESS_TOKEN_TYPE,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def create_refresh_token(
    user_id: UUID,
) -> str:
    """
    Create a JWT Refresh Token.

    Args:
        user_id: Authenticated user's UUID.

    Returns:
        Encoded JWT refresh token.
    """

    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload = {
        "sub": str(user_id),
        "type": REFRESH_TOKEN_TYPE,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def decode_token(
    token: str,
) -> dict:
    """
    Decode a JWT token.

    Args:
        token: JWT token.

    Returns:
        Decoded payload.

    Raises:
        JWTError: If token is invalid or expired.
    """

    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )