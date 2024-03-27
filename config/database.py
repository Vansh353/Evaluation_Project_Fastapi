from sqlalchemy import MetaData
from sqlalchemy.engine import create_engine 
import os
from dotenv import load_dotenv

load_dotenv(".env")

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

sqlalchemy_database_url = f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}"
engine = create_engine(sqlalchemy_database_url, pool_recycle=3600)

meta = MetaData()

with engine.connect() as connection:
    meta.reflect(connection)
    