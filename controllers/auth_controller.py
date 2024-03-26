from fastapi import Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_table import User
from dtos.auth_models import UserLogin, UserForgotPassword, UserPasswordReset
from utils.hashing import hash_password, verify
from fastapi.templating import Jinja2Templates
from helpers.token_helper import create_access_token
from helpers.api_helper import APIHelper
from helpers.email_helper import send_email

templates = Jinja2Templates(directory="templates")


def login_user(db: Session, user_dto: UserLogin):
    user = db.query(User).filter(User.email == user_dto.email).first()
    if not user:
        APIHelper.send_error_response("USER_NOT_FOUND")

    if not verify(user_dto.password, user.password):
        APIHelper.send_error_response("INVALID_PASSWORD")

    access_token = create_access_token(data={"sub": user.id})
    return APIHelper.send_success_response("Login Successful", data={"access_token": access_token})


async def forgot_password(db: Session, user_dto: UserForgotPassword):
    user = db.query(User).filter(User.email == user_dto.email).first()
    if not user:
        APIHelper.send_error_response("USER_NOT_FOUND")

    await send_email(user_dto.email, "Forgot Password", "forgot_password.html")

    return APIHelper.send_success_response("Email Sent Successfully")


def reset_password(db: Session, user_dto: UserPasswordReset):
    user = db.query(User).filter(User.email == user_dto.email).first()
    if not user:
        APIHelper.send_error_response("USER_NOT_FOUND")
    user.password = hash_password(user_dto.new_password)
    db.commit()

    return APIHelper.send_success_response("Password Reset Successful")
