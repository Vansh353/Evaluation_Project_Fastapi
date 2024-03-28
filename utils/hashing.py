from passlib.context import CryptContext
import jwt
from fastapi import HTTPException,status
from dotenv import dotenv_values
from sqlalchemy import select
from models.user_table import users_table
from config.database import engine
from sqlalchemy.orm import Session

config_credentials = dotenv_values(".env")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def verify_token_email(token: str):
    with engine.connect() as db:
        try:
            payload = jwt.decode(token, config_credentials['SECRET'],algorithms=['HS256'])
            stmt = select(users_table).where(users_table.c.id == payload['id'])
            user = db.execute(stmt).fetchone()
            return user
        except :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token",
                                headers={"WWW-Authenticate": "Bearer"})