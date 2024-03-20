# routes/user_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.user_controller import create_user
from dtos.user_models import UserSignupDTO

router = APIRouter(
   
    tags=['Signup']
)

@router.post("/signup")
def create_user_route(user_dto: UserSignupDTO, db: Session = Depends(get_db)):
   
    user = create_user(db, user_dto)
    return {"message": "User created successfully", "user": user}



