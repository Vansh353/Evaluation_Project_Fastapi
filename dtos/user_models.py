from pydantic import BaseModel, validator, EmailStr
from fastapi import HTTPException

class user_signup_dto(BaseModel):
    name: str
    password: str
    email: str
