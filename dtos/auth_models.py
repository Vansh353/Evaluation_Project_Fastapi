from datetime import datetime
from pydantic import BaseModel, validator, EmailStr
from fastapi import HTTPException
from datetime import datetime

class user_login(BaseModel):
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class UserModal(BaseModel):
    email:str
    name:str
    id: int 

class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    token: str