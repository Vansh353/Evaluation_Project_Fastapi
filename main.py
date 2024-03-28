# main.py
from fastapi import FastAPI
from routes.user import router as user_router  # Import the user router
from routes.auth import router as auth_router # Import the auth router
from routes.product import router as product_router # Import the product rout
from fastapi.middleware.cors import CORSMiddleware
from helpers.cors_helper import CORSHelper
app = FastAPI()

CORSHelper.setup_cors(app)
# Include the user router in your FastAPI application
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(product_router)






