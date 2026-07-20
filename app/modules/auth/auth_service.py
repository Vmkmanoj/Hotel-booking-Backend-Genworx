# ============================================================
# Third Party
# ============================================================

from sqlalchemy.ext.asyncio import AsyncSession

# ============================================================
# Local Imports
# ============================================================

from app.core.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.core.password import (
    hash_password,
    verify_password,
)

from app.modules.auth.auth_constants import (
    CUSTOMER,
    PROPERTY_OWNER,
)

from app.modules.auth.auth_exceptions import (
    InvalidCredentialsException,
    RoleNotFoundException,
    UserAlreadyExistsException,
)

from app.modules.auth.auth_repository import AuthRepository

from app.modules.auth.auth_schemas import (
    AuthResponse,
    CustomerRegisterRequest,
    MessageResponse,
    PropertyOwnerRegisterRequest,
)

from app.modules.users.models.users import User

from app.core.config import settings


class AuthService:

    def __init__(self, db: AsyncSession):

        self.repository = AuthRepository(db)

    # ========================================================
    # Customer Registration
    # ========================================================

    async def register_customer(
        self,
        request: CustomerRegisterRequest,
    ) -> MessageResponse:

        existing_user = await self.repository.get_user_by_email(
            request.email
        )

        if existing_user:
            raise UserAlreadyExistsException()

        role = await self.repository.get_role_by_name(
            CUSTOMER
        )

        if role is None:
            raise RoleNotFoundException()

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            password_hash=hash_password(request.password),
            role_id=role.id,
            is_active=True,
        )

        await self.repository.create_user(user)

        return MessageResponse(
            message="Customer registered successfully."
        )

    # ========================================================
    # Property Owner Registration
    # ========================================================

    async def register_property_owner(
        self,
        request: PropertyOwnerRegisterRequest,
    ) -> MessageResponse:

        existing_user = await self.repository.get_user_by_email(
            request.email
        )

        if existing_user:
            raise UserAlreadyExistsException()

        role = await self.repository.get_role_by_name(
            PROPERTY_OWNER
        )

        if role is None:
            raise RoleNotFoundException()

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone_number=request.phone_number,
            profile_image_url=request.profile_image_url,
            password_hash=hash_password(request.password),
            role_id=role.id,
            is_active=True,
        )

        await self.repository.create_user(user)

        return MessageResponse(
            message="Property owner registered successfully."
        )

    # ========================================================
    # Login
    # ========================================================

    async def login(
        self,
        email: str,
        password: str,
    ) -> AuthResponse:

        user = await self.repository.get_user_by_email(
            email
        )

        if user is None:
            raise InvalidCredentialsException()

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise InvalidCredentialsException()

        role = await self.repository.get_role_by_id(
            user.role_id
        )

        if role is None:
            raise RoleNotFoundException()

        access_token = create_access_token(
            user_id=str(user.id),
            role=role.name,
        )

        refresh_token = create_refresh_token(
            user_id=str(user.id),
        )

        return AuthResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="Bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            role=role.name,
        )
    

    # ========================================================
    # Refresh Access Token
    # ========================================================

    async def refresh_access_token(
        self,
        refresh_token: str,
    ) -> AuthResponse:
        """
        Validate a refresh token and generate a new access token.
        """

        payload = decode_token(refresh_token)

        if payload.get("type") != "refresh":   
            raise InvalidCredentialsException()

        user = await self.repository.get_user_by_id(
            payload["sub"],
        )

        if user is None:
            raise InvalidCredentialsException()

        if not user.is_active:
            raise InvalidCredentialsException()

        role = await self.repository.get_role_by_id(
            user.role_id,
        )

        if role is None:
            raise RoleNotFoundException()

        new_access_token = create_access_token(
            user_id=str(user.id),
            role=role.name,
        )

        return AuthResponse(
            access_token=new_access_token,
            refresh_token=refresh_token,
            token_type="Bearer",
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            role=role.name,
        )