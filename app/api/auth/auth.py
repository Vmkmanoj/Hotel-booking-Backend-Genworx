from fastapi import APIRouter , Depends 
from app.database import get_db
from app.schema.auth import CustomerRegister , PropertyRegister , RegisterResponse
from app.schema.login import LoginRequest ,LoginResponse
from app.services.auth_service import AuthService
from sqlalchemy.ext.asyncio import AsyncSession




authRouter = APIRouter()



@authRouter.post("/login", response_model=LoginResponse)
async def login(login: LoginRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    return await service.login(login)

@authRouter.post(
    "/property/register",
    response_model=RegisterResponse
)
async def property_register(
    owner: PropertyRegister,
    db: AsyncSession = Depends(get_db)
):
    service = AuthService(db)
    return await service.propertyOwnerRegister(owner)

@authRouter.post(
    "/customer/register",
    response_model=RegisterResponse
)
async def customer_register(
    user: CustomerRegister,
    db: AsyncSession = Depends(get_db)
):
    service = AuthService(db)
    return await service.customer_regsiter(user)


@authRouter.get("/")
async def getAuth():
    return "testing...."





