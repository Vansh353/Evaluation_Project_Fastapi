# Importing Libraries
from pydantic import BaseModel
from typing import Any, Optional

# Initializing
class BaseResponseModel(BaseModel):
    message: str
    data: Optional[Any]


class BaseErrorModel(BaseModel):
    data: Any
    error: Optional[str] = None
    def dict(self): #to convert it into dict
        return {"data": self.data, "error": self.error}
