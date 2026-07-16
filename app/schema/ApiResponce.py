from pydantic import BaseModel

class UserRegisterSuccess(BaseModel):
    message : str
    success : bool

class UserDetails(BaseModel):
    userName : str
    emailId : str
    roles : str

class loginSuccess(BaseModel):
    message : str
    access_token : str
    token_type : str
    userdetails : UserDetails


