from passlib.context import CryptContext
import jwt
from fastapi import HTTPException,status
from dotenv import dotenv_values
from models.user_table import User
from sqlalchemy.orm import Session

config_credentials = dotenv_values(".env")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def very_token(token: str, db: Session):
    try:
        payload = jwt.decode(token, config_credentials['SECRET'],algorithms=['HS256'])
        user = db.query(User).filter(User.id == payload['id']).first()
        return user
    except :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token",
                            headers={"WWW-Authenticate": "Bearer"})