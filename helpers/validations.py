from fastapi import HTTPException

def validate_user_data(user_dto):
    if not user_dto.email or "@" not in user_dto.email:
        raise HTTPException(status_code=400, detail="Invalid or empty email")
    
    if not user_dto.password:
        raise HTTPException(status_code=400, detail="Password cannot be empty")
     
    if not user_dto.name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")