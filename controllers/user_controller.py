from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user_table import User
from dtos.user_models import user_signup_dto
from utils.hashing import hash_password
from pydantic import EmailStr
from  helpers.db_helper import commit_to_db
from helpers.validations import validate_user_data
def create_user(db: Session, user_dto: user_signup_dto):
    
    validate_user_data(user_dto)
    
    
    hashed_password = hash_password(user_dto.password)
    
    user = User(
        name=user_dto.name,
        email=user_dto.email,
        password=hashed_password
    )

    commit_to_db(db, user)
    return {"message": "User created successfully", "user": user}
