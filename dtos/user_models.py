from datetime import datetime
from pydantic import BaseModel, Field

class UserSignupDto(BaseModel):
    name: str
    password: str
    email: str
    