from fastapi import Depends, HTTPException, Request,status
from sqlalchemy.orm import Session
from config.database import get_db
from models.user_table import User
from dtos.user_models import UserSignupDto
from utils.hashing import hash_password, very_token
from pydantic import EmailStr
from fastapi.templating import Jinja2Templates
from helpers.db_helper import commit_to_db
from helpers.validations import validate_user_data
from helpers.api_helper import APIHelper
from helpers.email_helper import send_email
templates=Jinja2Templates(directory="templates")
async def create_user(user_dto: UserSignupDto, db: Session):
    validate_user_data(user_dto)
    existing_user = db.query(User).filter(User.email == user_dto.email).first()
    if existing_user:
        return APIHelper.send_error_response("Email already signed up")
    hashed_password = hash_password(user_dto.password)
    user = User(
        name=user_dto.name,
        email=user_dto.email,
        
        password=hashed_password,
    )
    
    commit_to_db(db, user)
  
    await send_email(user_dto.email,"Account Veriication","signup.html", user)
  
   
    return APIHelper.send_success_response("User Created Successfully")



async def verify_email(request: Request, token: str, db: Session = Depends(get_db)):
    user = await very_token(token, db)
    if user and not user.is_verified:
        user.is_verified = True
        db.add(user)
        db.commit()
        return templates.TemplateResponse("verification.html", {"request": request,"name":user.name, "message": "Email Verified Successfully"}) 
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Already Verified.",
                        headers={"WWW-Authenticate": "Bearer"})