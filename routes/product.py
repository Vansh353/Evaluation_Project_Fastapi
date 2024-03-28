# routes/product.py
from typing import Optional
from fastapi import APIRouter, Depends, Query
from controllers.product_controller import create_product,product_search
from helpers.token_helper import get_current_user
from dtos.product_models import ProductModel,ProductSearch
router = APIRouter(
   
    tags=['Product']
)

@router.post('/create_product')
def create_product_route(request: ProductModel,token: str = Depends(get_current_user)):
    return create_product(request,token)
@router.get('/search_product')
def search_product_route(name: Optional[str] = Query(None), category: Optional[str] = Query(None)):
    return product_search(name, category)