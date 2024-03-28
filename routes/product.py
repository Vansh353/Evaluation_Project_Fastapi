# routes/product.py
from fastapi import APIRouter, Depends
from controllers.product_controller import create_product
from helpers.token_helper import get_token,get_current_user
from dtos.product_models import ProductModel
router = APIRouter(
   
    tags=['Product']
)

@router.post('/create_product')
def create_product_route(request: ProductModel,token: str = Depends(get_current_user)):
    return create_product(request,token)
