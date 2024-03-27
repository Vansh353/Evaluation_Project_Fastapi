from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from dotenv import load_dotenv
from dtos.auth_models import UserModal
from helpers.db_helper import get_user_by_id
from helpers.api_helper import APIHelper
import os
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

bearer_scheme = HTTPBearer(auto_error=False)
load_dotenv(".env")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY=os.getenv("JWT_SECRET") ##secret key to genrate jwt token
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  #for creating jwt token we need two things secret key and user id usng that we can access in future
    return encoded_jwt

def verify_token(token: str) -> UserModal:

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id: int = payload.get("id")
    if user_id is None:
        APIHelper.send_unauthorized_error(errorMessageKey='Unauthorized')
    
    user =get_user_by_id(user_id)
    if user is None:
        APIHelper.send_unauthorized_error(
            errorMessageKey='Unauthorized')
    return UserModal(**user._mapping)

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserModal:
    return verify_token(token)

async def get_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    return credentials.credentials