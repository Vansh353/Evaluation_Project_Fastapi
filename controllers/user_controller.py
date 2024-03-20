# controllers/user_controller.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user_table import User
from dtos.user_models import UserSignupDTO
from utils.hashing import hash_password
from pydantic import EmailStr
def create_user(db: Session, user_dto: UserSignupDTO):
    
    if not user_dto.email or "@" not in user_dto.email:
        raise HTTPException(status_code=400, detail="Invalid or empty email")
    
    if not user_dto.password:
        raise HTTPException(status_code=400, detail="Password cannot be empty")
     
    if not user_dto.name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    hashed_password = hash_password(user_dto.password)
    
   
    user = User(
        Name=user_dto.name,
        Email=user_dto.email,
        EncryptedPassword=hashed_password
    )

   
    db.add(user)
    db.commit()
    db.refresh(user)
    return user




