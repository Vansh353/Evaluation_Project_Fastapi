from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user_table import User
from dtos.user_models import user_signup_dto
from utils.hashing import hash_password
from pydantic import EmailStr
from  helpers.db_helper import commit_to_db

def create_user(db: Session, user_dto: user_signup_dto):
    
    if not user_dto.email or "@" not in user_dto.email:
        raise HTTPException(status_code=400, detail="Invalid or empty email")
    
    if not user_dto.password:
        raise HTTPException(status_code=400, detail="Password cannot be empty")
     
    if not user_dto.name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    hashed_password = hash_password(user_dto.password)
    
    user = User(
        name=user_dto.name,
        email=user_dto.email,
        password=hashed_password
    )

    commit_to_db(db, user)
    return {"message": "User created successfully", "user": user}
