from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.user_controller import create_user, verify_email
from dtos.user_models import UserSignupDto
from fastapi.responses import HTMLResponse

router = APIRouter(tags=['Signup'])

@router.post("/signup")
async def create_user_route(user_dto: UserSignupDto, db: Session = Depends(get_db)):
   return await create_user(user_dto, db)

@router.get("/verification",response_class=HTMLResponse)
async def verify_email_route(request: Request, token: str, db: Session = Depends(get_db)):
    return await verify_email(request, token, db)