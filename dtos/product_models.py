from pydantic import BaseModel,validator
from typing import Optional
from helpers.validations import validate_product_name, validate_product_category, validate_product_price

class ProductModel(BaseModel):
    name: str 
    category: str 
    description: Optional[str] = None
    price: float
    rating: Optional[float] = 0
    discount: Optional[float] = 0

    _name = validator("name", allow_reuse=True)(validate_product_name)
    _category = validator("category", allow_reuse=True)(validate_product_category)
    _price = validator("price", allow_reuse=True)(validate_product_price)