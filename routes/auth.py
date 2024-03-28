# routes/user_routes.py
from fastapi import APIRouter, Depends
from controllers.auth_controller import login_user,forgot_password,reset_password
from dtos.auth_models import UserLogin,UserForgotPassword,UserPasswordReset
from helpers.token_helper import get_token
router = APIRouter(
   
    tags=['Login']
)

@router.post('/login')
def login_user_route(request: UserLogin):
    return login_user(request)

@router.post('/forgot_password')
async def forgot_password_route(request:UserForgotPassword):
    return await forgot_password(request)

@router.post('/reset_password')
def reset_password_route(request:UserPasswordReset,token: str = Depends(get_token)):
    return  reset_password(request,token)