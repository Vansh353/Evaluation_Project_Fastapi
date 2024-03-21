from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_table import User
from dtos.auth_models import user_login
from utils.hashing import hash_password, verify
from helpers.token_helper import create_access_token
from pydantic import EmailStr
from helpers.validations import validate_user_data
from helpers.api_helper import APIHelper

def login_user(db: Session, user_dto: user_login):
    user = db.query(User).filter(User.email == user_dto.email).first()
    if not user:
        APIHelper.send_error_response("USER_NOT_FOUND")
    
    if not verify(user_dto.password, user.password):
        APIHelper.send_error_response("INVALID_PASSWORD")
        
    access_token = create_access_token(data={"sub": user.id})
   
    return APIHelper.send_success_response("Login Successful", data={"access_token": access_token})


