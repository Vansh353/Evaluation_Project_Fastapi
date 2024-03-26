from pydantic import BaseModel, Field,EmailStr
from typing import List
class UserSignupDto(BaseModel):
    name: str
    password: str
    email: str

