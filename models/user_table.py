from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# Importing libraries
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, Text, Boolean
from config.database import meta


# Base = declarative_base()
# class User(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     email = Column(String(255), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     is_verified=Column(Boolean, default=False)
#     created_at = Column(DateTime, default=datetime.now())  
#     updated_at = Column(DateTime, default=datetime.now())


# Initializing
users_table = Table(
    "user",
    meta,
    Column("id", Integer, primary_key=True,autoincrement=True),
    Column("name", Text, nullable=False),
    Column("email", Text,unique=True,nullable=False),
    Column("password", Text,nullable=False),
    Column("is_verified", Boolean,default=False),
    Column("created_at", DateTime,default=datetime.now()),
    Column("updated_at", DateTime,default=datetime.now()),
    extend_existing=True
)