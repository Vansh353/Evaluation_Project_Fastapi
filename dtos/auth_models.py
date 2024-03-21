from pydantic import BaseModel, validator, EmailStr
from fastapi import HTTPException

class user_login(BaseModel):
    email: EmailStr
    password: str
       

class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    token: str