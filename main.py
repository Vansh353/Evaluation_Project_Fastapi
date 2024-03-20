# main.py
from fastapi import FastAPI
from routes.user import router as user_router  # Import the user router

app = FastAPI()

# Include the user router in your FastAPI application
app.include_router(user_router)
