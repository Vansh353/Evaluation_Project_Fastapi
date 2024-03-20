from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = "mysql+mysqlconnector://root:vansh2003@localhost/sea_basket"

engine = create_engine(sqlalchemy_database_url)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db() -> Session:
    db = session_local()
    try:
        yield db
    finally:
        db.close()
