from config.database import engine
from models.user_table import User
from sqlalchemy.orm import Session
def commit_to_db(db: Session, instance):
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()
