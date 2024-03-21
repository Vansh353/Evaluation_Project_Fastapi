# routes/user_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.auth_controller import login_user
from dtos.auth_models import user_login

router = APIRouter(
   
    tags=['Login']
)

@router.post('/login')
def login_user_route(user_dto: user_login,db: Session = Depends(get_db)):
    return login_user(db, user_dto)


