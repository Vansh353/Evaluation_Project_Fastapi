from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_table import User
from dtos.user_models import user_signup_dto
from utils.hashing import hash_password
from pydantic import EmailStr
from  helpers.db_helper import commit_to_db
from helpers.validations import validate_user_data
from helpers.api_helper import APIHelper
def create_user(db: Session, user_dto: user_signup_dto):
    
    validate_user_data(user_dto)
    
    # Check if user already exists in the database
    existing_user = db.query(User).filter(User.email == user_dto.email).first()
    if existing_user:
        return APIHelper.send_error_response("Email already signed up")
    
    hashed_password = hash_password(user_dto.password)
    
    user = User(
        name=user_dto.name,
        email=user_dto.email,
        password=hashed_password,
        created_at=user_dto.created_at,
        updated_at=user_dto.updated_at
        
    )

    commit_to_db(db, user)
    return APIHelper.send_success_response("User Created Successfully")
