from pydantic import BaseModel, validator, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str
  

class UserModal(BaseModel):
    email:str
    name:str
    id: int 

class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    token: str
    
class UserPasswordReset(BaseModel):
    email: str
    new_password: str
    
class UserForgotPassword(BaseModel):
    email: str
    