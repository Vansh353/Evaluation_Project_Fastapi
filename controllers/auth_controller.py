from sqlalchemy import select
from config.database import engine
from models.user_table import users_table
from dtos.auth_models import UserLogin, UserForgotPassword, UserPasswordReset
from utils.hashing import hash_password, verify
from fastapi.templating import Jinja2Templates
from helpers.token_helper import create_access_token
from utils.hashing import verify_token_email
from helpers.api_helper import APIHelper
from helpers.email_helper import send_email

templates = Jinja2Templates(directory="templates")


def login_user(request: UserLogin):
    with engine.connect() as db:
        user = db.execute(select(users_table).where(users_table.c.email == request.email)).fetchone()
        if not user:
            return APIHelper.send_error_response(errorMessageKey="User Not Found")
        
        if user and not user.is_verified:
            return APIHelper.send_error_response(errorMessageKey="User Not Verified")

        if user and not verify(request.password, user.password):
            return APIHelper.send_error_response(errorMessageKey="Invalid password")

        access_token = create_access_token(data={"sub": user.id})
    return APIHelper.send_success_response(data={"access_token": access_token},successMessageKey="Login Successfully")

    

async def forgot_password(request: UserForgotPassword):
    with engine.connect() as db:
        
        user = db.execute(select(users_table).where(users_table.c.email == request.email)).fetchone()
        if not user:
            return APIHelper.send_error_response(errorMessageKey="User Not Found")
        token=await send_email(request.email, "Forgot Password", "forgot_password.html",user)

    return APIHelper.send_success_response(data={"token": token}, successMessageKey='Email Sent Successfully')

def reset_password(request: UserPasswordReset, token: str):
    
    with engine.connect() as db:
        token_data = verify_token_email(token)
        user = db.execute(select(users_table).where(users_table.c.id == token_data.id)).fetchone()
        if not user:
            return APIHelper.send_error_response(errorMessageKey="User Not Found")
        
        hashed_password = hash_password(request.new_password)  # Hash the new password
        db.execute(users_table.update().where(users_table.c.id == token_data.id).values(password=hashed_password))
        db.commit()

    return APIHelper.send_success_response(successMessageKey="Password Reset Successful")
