# routes/user_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.user_controller import create_user
from dtos.user_models import user_signup_dto

router = APIRouter(
   
    tags=['Signup']
)

@router.post("/signup")
def create_user_route(user_dto: user_signup_dto, db: Session = Depends(get_db)):
   return create_user(db, user_dto)



