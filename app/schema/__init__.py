from app.schema.ApiResponce import UserDetails , UserRegisterSuccess , loginSuccess
from app.schema.user import UserBase , UserCreate , UserResponse , UserUpdate 
from app.schema.auth import CustomerRegister , PropertyRegister , RegisterResponse
from app.schema.login import LoginRequest ,LoginResponse
__all__ = [
    "UserDetails",
    "UserRegisterSuccess",
    "loginSuccess", "UserBase",
    "UserCreate",
    "UserResponse",
    "UserUpdate" ,
    "CustomerRegister" ,
    "PropertyRegister" , 
    "RegisterResponse" ,
    "LoginRequest",
    "LoginResponse"
]