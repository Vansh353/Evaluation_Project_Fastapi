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


def validate_product_name(name: str):
    if not name or name.strip() == "":
        raise HTTPException(status_code=400, detail="Product name cannot be empty")
    return name

def validate_product_category(category: str):
    if not category or category.strip() == "":
        raise HTTPException(status_code=400, detail="Product category cannot be empty")
    return category

def validate_product_price(price: float):
    if price is None or price <= 0:
        raise HTTPException(status_code=400, detail="Product price must be greater than 0")
    return price
