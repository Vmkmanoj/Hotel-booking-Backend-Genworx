from fastapi import APIRouter , Depends , HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schema.ApiResponce import UserRegisterSuccess ,loginSuccess ,UserDetails
from app.schema.user import UserCreate 
from app.models.users import User
from app.utils.passwordhashing import hash_password ,verify_password
from app.utils.jwt import create_access_token
authRouter = APIRouter()


@authRouter.post("/login",response_model= loginSuccess)
def login(user : UserCreate , db : Session = Depends(get_db)):

    userRespone = db.query(User).filter(user.email == User.email).first()

    if not userRespone:
        raise HTTPException(status_code=401,detail= "Invalid credentials")
    
    if not verify_password(user.Password , userRespone.Password):
        raise HTTPException(status_code=401,detail= "Invalid credentials")
    
    token_data = {
        "user_id": str(userRespone.Id),
        "email": userRespone.email
    }

    access_token = create_access_token(
       token_data
    )

    return loginSuccess(
        message= "login success" ,
        access_token = access_token , 
        token_type= "bearer" ,
        userdetails= UserDetails(
        username=userRespone.first_name,
        emailId=userRespone.email,
    ))


# @authRouter.post("/register",response_model=UserRegisterSuccess)
# def register(userRegister : UserRegister, db : Session = Depends(get_db)):
#     usersCheck = db.query(Users).filter(Users.Email == userRegister.Email).first()

#     if usersCheck:
#         raise HTTPException(status_code=400,detail="users already register...!")

#     userResponse = Users(
#         Name=userRegister.Name,
#         Qualification = userRegister.Qualification,
#         Specialization = userRegister.Specialization,
#         Email = userRegister.Email,
#         PhoneNumber = userRegister.PhoneNumber,
#         HospitalName = userRegister.HospitalName,
#         RegistrationNumber = userRegister.RegistrationNumber,
#         Password = hash_password(userRegister.Password),
#         Roles = userRegister.Roles,
#         Status = "Non-Available"
#     )
    
#     db.add(userResponse)
#     db.commit()

#     return UserRegisterSuccess(message="Register success..!",success=True)



@authRouter.get("/")
def getAuth():
    return "testing...."





