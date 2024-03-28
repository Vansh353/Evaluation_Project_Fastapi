from typing import Optional
from config.database import engine
from sqlalchemy import select
from helpers.api_helper import APIHelper
from models.product_table import product_table
from models.user_table import users_table
from dtos.product_models import ProductModel




def create_product(request:ProductModel, token: str):
    with engine.connect() as db:
        existing_product = db.execute(select(product_table).where(product_table.c.name == request.name)).fetchone()
        if existing_product:
            return APIHelper.send_error_response(errorMessageKey="Product already exists")

        new_product = db.execute(product_table.insert().values(
                name=request.name, category=request.category,description=request.description,price=request.price,rating=request.rating,discount=request.discount))
        db.commit()        
    return APIHelper.send_success_response(successMessageKey="Product Created Successfully")

def product_search(name: Optional[str] = None, category: Optional[str] = None):
    with engine.connect() as db:
        query = select(product_table)
        if name or category:
            query = query.where(
            (product_table.c.name.like(f"%{name}%")) if name else True,
            (product_table.c.category.like(f"%{category}%")) if category else True
            )
        products = db.execute(query).fetchall()
        if not products:
            return APIHelper.send_error_response(errorMessageKey="Product or Category Not Found")
        return APIHelper.send_success_response(data=[ProductModel(**row._mapping) for row in products], successMessageKey="Product Found")