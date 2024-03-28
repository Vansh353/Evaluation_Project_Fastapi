from fastapi import Depends, Request
from config.database import engine
from dtos.user_models import UserSignupDto
from utils.hashing import hash_password, verify_token_email
from pydantic import EmailStr
from fastapi.templating import Jinja2Templates
from helpers.api_helper import APIHelper
from helpers.email_helper import send_email
from models.user_table import users_table
templates=Jinja2Templates(directory="templates")
from sqlalchemy import select

async def create_user(request: UserSignupDto):
    with engine.connect() as db:
        # Hash the password
        existing_user = db.execute(select(users_table).where(users_table.c.email == request.email)).fetchone()
        if existing_user:
           return  APIHelper.send_error_response(errorMessageKey="User already exists")
        
        hashed_password = hash_password(request.password)

        new_user = db.execute(users_table.insert().values(
                email=request.email, password=hashed_password,name=request.name))
        db.commit()
        result = new_user.lastrowid
        new_user_id = db.execute(users_table.select().where(users_table.c.id == result)).fetchone()
        
        token =await send_email(request.email,"Account Verification","signup.html", new_user_id)

    return APIHelper.send_success_response(data={"token": token}, successMessageKey='User Created Successfully')
  



def verify_email(request: Request, token: str):
    with engine.connect() as db:
        user =  verify_token_email(token)
        if user and not user.is_verified:
            db.execute(users_table.update().where(users_table.c.id == user.id).values(is_verified=True))
            db.commit()
            return  APIHelper.send_success_response(successMessageKey="Email Verification Successfully")
        return APIHelper.send_success_response(successMessageKey="Already Verified")