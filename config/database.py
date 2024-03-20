# config/database.py
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'user', 'password', 'localhost', and 'dbname' with your MySQL credentials and database name
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:vansh2003@localhost/sea_basket"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
