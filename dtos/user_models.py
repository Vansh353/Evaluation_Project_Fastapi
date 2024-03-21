from datetime import datetime
from pydantic import BaseModel, Field

class user_signup_dto(BaseModel):
    name: str
    password: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)