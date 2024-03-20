from pydantic import BaseModel, validator, EmailStr
from fastapi import HTTPException

class UserSignupDTO(BaseModel):
    name: str
    password: str
    email: str

  