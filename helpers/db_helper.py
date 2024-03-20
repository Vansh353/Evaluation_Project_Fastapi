
from sqlalchemy.orm import Session
def commit_to_db(db: Session, instance):
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance