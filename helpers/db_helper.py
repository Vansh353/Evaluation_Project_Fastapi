from sqlalchemy import select
from config.database import engine
from models.user_table import users_table
from sqlalchemy.orm import Session
# def commit_to_db(db: Session, instance):
#     db.add(instance)
#     db.commit()
#     db.refresh(instance)
#     return instance


def get_user_by_id(id: int):
    with engine.connect() as db:
        return db.execute(select(users_table).where(users_table.c.id == id)).fetchone()
