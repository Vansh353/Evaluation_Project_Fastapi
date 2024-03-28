# user_dto.py

from typing import Optional
from pydantic import BaseModel, validator
from helpers.validations import validate_email, validate_password, validate_name

class UserSignupDto(BaseModel):
    name: str
    password: str
    email: str

    _name = validator("name", allow_reuse=True)(validate_name)
    _password = validator("password", allow_reuse=True)(validate_password)
    _email = validator("email", allow_reuse=True)(validate_email)