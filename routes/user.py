from fastapi import APIRouter, Depends
from config.database import engine
from controllers.user_controller import create_user, verify_email
from dtos.user_models import UserSignupDto
from helpers.token_helper import get_token
from fastapi import APIRouter, Depends, Request

router = APIRouter(tags=['Signup'])

@router.post("/signup")
async def create_user_route(request: UserSignupDto):
   return await create_user(request)




@router.get("/verify-email")
async def verify_email_route(request: Request, token: str = Depends(get_token)):
    return await verify_email(request, token)
 

