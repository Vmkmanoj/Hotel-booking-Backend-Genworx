# ============================================================
# Third Party
# ============================================================

from uuid import UUID

# ============================================================
# Local Imports
# ============================================================

from app.common.enums.user_status import UserStatus

from app.modules.users.users_repository import UsersRepository

from app.modules.users.users_schemas import (
    CurrentUserResponse,
    UpdateProfileRequest,
    UserListResponse,
    UserMessageResponse,
    UserResponse,
    UpdateUserRequest,
)

from app.modules.users.models.users import User

from app.modules.users.users_exceptions import (
    UserNotFoundException,
)


class UsersService:

    def __init__(
        self,
        repository: UsersRepository,
    ):
        self.repository = repository

    async def get_my_profile(
        self,
        current_user: User,
    ) -> CurrentUserResponse:
        """
        Return the authenticated user's profile.
        """

        return CurrentUserResponse.model_validate(
            current_user
        )
    
    # ============================================================
    # Update My Profile
    # ============================================================

    async def update_my_profile(
        self,
        current_user: User,
        request: UpdateProfileRequest,
    ) -> CurrentUserResponse:
        """
        Update the authenticated user's profile.
        """

        update_data = request.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():

            setattr(
                current_user,
                field,
                value,
            )

        updated_user = await self.repository.save_user(
            current_user,
        )

        return CurrentUserResponse.model_validate(
            updated_user,
        )
    
    # ========================================================
    # Get All Users - Admin Functionalities
    # ========================================================

    async def get_all_users(
        self,
    ) -> UserListResponse:
        """
        Return all users.
        """

        users = await self.repository.get_all_users()

        total = await self.repository.count_users()

        response = [
            UserResponse.model_validate(
                user,
            )
            for user in users
        ]

        return UserListResponse(
            users=response,
            total=total,
        )


    # ========================================================
    # Get User By ID
    # ========================================================

    async def get_user_by_id(
        self,
        user_id: UUID,
    ) -> UserResponse:
        """
        Return a user by ID.
        """

        user = await self.repository.get_user_by_id(
            user_id,
        )

        if user is None:
            raise UserNotFoundException()

        return UserResponse.model_validate(
            user,
        )
    
    # ========================================================
    # Update User
    # ========================================================

    async def update_user(
        self,
        user_id: UUID,
        request: UpdateUserRequest,
    ) -> UserResponse:
        """
        Update a user's profile.
        """

        user = await self.repository.get_user_by_id(
            user_id,
        )

        if user is None:
            raise UserNotFoundException()

        update_data = request.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():

            setattr(
                user,
                field,
                value,
            )

        updated_user = await self.repository.save_user(
            user,
        )

        return UserResponse.model_validate(
            updated_user,
        )

    # ========================================================
    # Update User Status (Private)
    # ========================================================

    async def _update_user_status(
        self,
        user_id: UUID,
        status: UserStatus,
    ) -> UserResponse:
        """
        Update the lifecycle status of a user.
        """

        user = await self.repository.get_user_by_id(
            user_id,
        )

        if user is None:
            raise UserNotFoundException()

        user.user_status = status

        updated_user = await self.repository.save_user(
            user,
        )

        return UserResponse.model_validate(
            updated_user,
        )
    
    # ========================================================
    # Activate User
    # ========================================================

    async def activate_user(
        self,
        user_id: UUID,
    ) -> UserResponse:
        """
        Activate a user account.
        """

        return await self._update_user_status(
            user_id,
            UserStatus.ACTIVE,
        )
    
    # ========================================================
    # Suspend User
    # ========================================================

    async def suspend_user(
        self,
        user_id: UUID,
    ) -> UserResponse:
        """
        Suspend a user account.
        """

        return await self._update_user_status(
            user_id,
            UserStatus.SUSPENDED,
        )
    
    # ========================================================
    # Deactivate User
    # ========================================================

    async def deactivate_user(
        self,
        user_id: UUID,
    ) -> UserResponse:
        """
        Deactivate a user account.
        """

        return await self._update_user_status(
            user_id,
            UserStatus.DEACTIVATED,
        )