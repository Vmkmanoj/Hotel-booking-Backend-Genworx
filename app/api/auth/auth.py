from fastapi import APIRouter , Depends 
from app.database import get_db
from app.schema.auth import CustomerRegister , PropertyRegister , RegisterResponse
from app.schema.login import LoginRequest ,LoginResponse
from app.services.auth_service import AuthService
from sqlalchemy.ext.asyncio import AsyncSession

authRouter = APIRouter()



@authRouter.post("/login", response_model=LoginResponse)
async def login(login: LoginRequest, db: AsyncSession = Depends(get_db)):
    return await db.run_sync(lambda s: AuthService(s).login(login))


@authRouter.post(
    "/property/register",
    response_model=RegisterResponse
)
async def property_register(
    owner: PropertyRegister,
    db: AsyncSession = Depends(get_db)
):
    return await db.run_sync(lambda s: AuthService(s).propertyOwnerRegister(owner))

@authRouter.post(
    "/customer/register",
    response_model=RegisterResponse
)
async def customer_register(
    user: CustomerRegister,
    db: AsyncSession = Depends(get_db)
):
    return await db.run_sync(lambda s: AuthService(s).customer_regsiter(user))


@authRouter.get("/")
async def getAuth():
    return "testing...."





