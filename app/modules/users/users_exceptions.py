# ============================================================
# Third Party
# ============================================================

from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    """
    Raised when the requested user does not exist.
    """

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )