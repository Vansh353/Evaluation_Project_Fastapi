from pydantic import BaseModel, validator, EmailStr
from pydantic import BaseModel, validator
from helpers.validations import validate_email, validate_password
class UserLogin(BaseModel):
    email: EmailStr
    password: str 
    _password = validator("password", allow_reuse=True)(validate_password)
    _email = validator("email", allow_reuse=True)(validate_email)
  

class UserModal(BaseModel):
    email:str
    name:str
    id: int 
    is_verified: bool

class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    token: str
    
class UserPasswordReset(BaseModel):
   
    new_password: str
   
    
class UserForgotPassword(BaseModel):
    email: str
    _email = validator("email", allow_reuse=True)(validate_email)
  

    
    