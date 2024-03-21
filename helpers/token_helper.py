
from datetime import datetime, timedelta
import jwt
from typing import Optional


SECRET_KEY = "d8d9935ca4abc62e71480e1185bf1b31f011ed1a1591a914364f9b0a44009882" ##secret key to genrate jwt token
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

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) ##to decode the jwt token we verify token mehtd
        return payload
    except jwt.JWTError:
        return None
