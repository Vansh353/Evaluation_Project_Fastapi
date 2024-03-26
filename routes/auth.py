# routes/user_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.auth_controller import login_user,forgot_password,reset_password
from dtos.auth_models import UserLogin,UserForgotPassword,UserPasswordReset

router = APIRouter(
   
    tags=['Login']
)

@router.post('/login')
def login_user_route(user_dto: UserLogin,db: Session = Depends(get_db)):
    return login_user(db, user_dto)
@router.post('/forgot_password')
async def forgot_password_route(user_dto:UserForgotPassword ,db: Session=Depends(get_db)):
    return await forgot_password(db, user_dto)

@router.post('/reset_password')
def reset_password_route(user_dto:UserPasswordReset,db: Session=Depends(get_db)):
    return reset_password(db, user_dto)