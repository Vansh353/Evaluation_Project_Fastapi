from datetime import datetime
from sqlalchemy import DECIMAL, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from sqlalchemy.sql import func
# Importing libraries
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, Text, Boolean
from config.database import meta

product_table = Table(
    "product",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("category", String(255), nullable=False),
    Column("description", Text),
    Column("price", DECIMAL(10,2), nullable=False),
    Column("rating", DECIMAL(3,2), default=0),
    Column("discount", DECIMAL(5,2), default=0),
    Column("created_at", DateTime,default=datetime.now()),
    Column("updated_at", DateTime,default=datetime.now()),
    extend_existing=True
)

