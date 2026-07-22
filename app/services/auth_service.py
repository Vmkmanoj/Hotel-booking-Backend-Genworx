from app.repositories.auth_repositories import AuthRepository
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.utils.passwordhashing import verify_password
from app.utils.jwt import create_access_token
from app.models.permissions import Permission
from app.models.roles_permission import RolePermission
from app.schema.login import  LoginResponse
from app.models.users import User
from app.models.roles import Role
from app.utils.passwordhashing import hash_password
from app.schema.auth import  RegisterResponse


class AuthService:

    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = AuthRepository(db)

    async def login(self, request):

        user = await self.repo.get_user_by_email(request.email)

        if not user:
            raise HTTPException(401, "User not found")

        if not verify_password(request.password, user.password_hash):
            raise HTTPException(401, "Invalid password")
        
        role = await self.repo.get_user_role(user.role_id)

        permissions_result = await self.db.execute(
            select(Permission)
            .join(RolePermission, Permission.id == RolePermission.permission_id)
            .where(RolePermission.rolesId == role.id)
        )
        permissions = permissions_result.scalars().all()

        permission_list = [permission.name for permission in permissions]

        access_token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role": role.name,
            "role_id": str(role.id),
            "permissions": permission_list
        }
        )

        return LoginResponse(
            success=True,
            message="Login successful",
            role = role.name ,
            access_token=access_token,
            token_type="Bearer"
        )
    
    async def propertyOwnerRegister(self, request):

        existing_user = await self.repo.get_user_by_email(request.email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered."
            )

        owner_role = await self.repo.get_role_by_name("PROPERTY_OWNER")

        if not owner_role:
            raise HTTPException(
                status_code=404,
                detail="Owner role not found."
            )

        new_owner = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            phone=request.phone,
            avatar_url=request.avatar_url,
            created_by = request.email,
            updated_by = request.email,
            password_hash=hash_password(request.password),
            role_id=owner_role.id,
            is_active=True
        )

        self.db.add(new_owner)
        await self.db.commit()

        return RegisterResponse(
            success=True,
            message="Property owner registered successfully."
        )
    
    async def customer_regsiter(self,request):

        existing_user = await self.repo.get_user_by_email(request.email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered."
            )

        customer_role = await self.repo.get_role_by_name("CUSTOMER")

        if not customer_role:
            raise HTTPException(
                status_code=404,
                detail="Customer role not found."
            )

        new_user = User(
            first_name = request.userName,
            email = request.email,
            password_hash=hash_password(request.password),
            role_id=customer_role.id,
            is_active=True,
            created_by = request.email,
            updated_by = request.email
        )

        self.db.add(new_user)
        await self.db.commit()

        return RegisterResponse(
            success=True,
            message="Customer registered successfully."
        )
