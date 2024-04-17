from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session
from app.models import Meats
from app.schemas import Meats_schema


def get_meats(db: Session):
    return db.query(Meats).all()


def get_meat_by_id(db: Session, meat_id: UUID):
    return db.query(Meats).filter(Meats.id == meat_id).first()


def create_meat(db: Session, meat: Meats_schema):
    _meat = Meats(
        name=meat.name,
        price=meat.price,
        img_url=meat.img_url,
        created_at=datetime.now(),
    )
    db.add(_meat)
    db.commit()
    db.refresh(_meat)
    return


def delete_meat(db: Session, meat_id: UUID):
    db.query(Meats).filter(Meats.id == meat_id).delete()
    db.commit()
    return


def update_meat(db: Session, meat_id: UUID, meat: Meats_schema):
    _meat = get_meat_by_id(db, meat_id)
    _meat.name = meat.name
    _meat.price = meat.price
    _meat.updated_at = datetime.now()
    return
