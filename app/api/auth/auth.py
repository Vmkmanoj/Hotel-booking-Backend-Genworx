from fastapi import APIRouter , Depends , HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schema.auth import CustomerRegister , PropertyRegister , RegisterResponse
from app.models.roles import Role
from app.schema.login import LoginRequest ,LoginResponse
from app.models.users import User
from app.utils.passwordhashing import hash_password 
from app.services.auth_service import AuthService



authRouter = APIRouter()



@authRouter.post("/login", response_model=LoginResponse)
def login(login: LoginRequest, db: Session = Depends(get_db)):
    
    authService = AuthService(db)

    return authService.login(login)


@authRouter.post(
    "/property/register",
    response_model=RegisterResponse
)
def property_register(
    owner: PropertyRegister,
    db: Session = Depends(get_db)
):
    authService = AuthService(db)
    
    return authService.propertyOwnerRegister(owner)

@authRouter.post(
    "/customer/register",
    response_model=RegisterResponse
)
def customer_register(
    user: CustomerRegister,
    db: Session = Depends(get_db)
):
    authService = AuthService(db)
    
    return authService.customer_regsiter(user)


@authRouter.get("/")
def getAuth():
    return "testing...."





