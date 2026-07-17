from fastapi import APIRouter , Depends , HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schema.auth import CustomerRegister , PropertyRegister , RegisterResponse
from app.models.roles import Role
from app.schema.login import LoginRequest ,LoginResponse
from app.models.users import User
from app.models.permissions import Permission
from app.models.roles_permission import RolePermission
from app.utils.passwordhashing import hash_password ,verify_password
from app.utils.jwt import create_access_token


authRouter = APIRouter()


@authRouter.post("/login", response_model=LoginResponse)
def login(login: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == login.email).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(login.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Account is inactive"
        )

    role = db.query(Role).filter(Role.id == user.role_id).first()

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    permissions = (
        db.query(Permission)
        .join(
            RolePermission,
            Permission.id == RolePermission.permission_id
        )
        .filter(RolePermission.rolesId == role.id)
        .all()
    )

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


@authRouter.post(
    "/property/register",
    response_model=RegisterResponse
)
def property_register(
    owner: PropertyRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == owner.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    owner_role = db.query(Role).filter(
        Role.name == "PROPERTY_OWNER"
    ).first()

    if not owner_role:
        raise HTTPException(
            status_code=404,
            detail="Owner role not found."
        )

    new_owner = User(
        first_name=owner.first_name,
        last_name=owner.last_name,
        email=owner.email,
        phone=owner.phone,
        avatar_url=owner.avatar_url,
        created_by = owner.email,
        updated_by = owner.email,
        password_hash=hash_password(owner.password),
        role_id=owner_role.id,
        is_active=True
    )

    db.add(new_owner)
    db.commit()

    return RegisterResponse(
        success=True,
        message="Property owner registered successfully."
    )

@authRouter.post(
    "/customer/register",
    response_model=RegisterResponse
)
def customer_register(
    user: CustomerRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    customer_role = db.query(Role).filter(
        Role.name == "CUSTOMER"
    ).first()

    if not customer_role:
        raise HTTPException(
            status_code=404,
            detail="Customer role not found."
        )

    new_user = User(
        first_name = user.userName,
        email = user.email,
        password_hash=hash_password(user.password),
        role_id=customer_role.id,
        is_active=True,
        created_by = user.email,
        updated_by = user.email
    )

    db.add(new_user)
    db.commit()

    return RegisterResponse(
        success=True,
        message="Customer registered successfully."
    )


@authRouter.get("/")
def getAuth():
    return "testing...."





