# validations.py

from fastapi import HTTPException

def validate_email(email: str):
    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail="Invalid or empty email")
    return email

def validate_password(password: str):
    if not password:
        raise HTTPException(status_code=400, detail="Password cannot be empty")
    return password

def validate_name(name: str):
    if not name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    return name