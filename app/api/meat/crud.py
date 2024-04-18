from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session
from app.models import Meats, Needed_products
from app.schemas import Meats_schema


def get_meats(db: Session):
    meats_with_needed_products = (
        db.query(Meats, Needed_products)
        .join(Needed_products, Meats.id == Needed_products.meat_id, isouter=False)
        .all()
    )
    result = []
    for meat, _ in meats_with_needed_products:
        _meat = {
            "id": meat.id,
            "name": meat.name,
            "price": meat.price,
            "img_url": meat.img_url,
            "needed_products": [],
        }
        if _meat not in result:
            result.append(_meat)

    for _, needed_product in meats_with_needed_products:
        for i, e in enumerate(result):
            if e["id"] == needed_product.meat_id:
                result[i]["needed_products"].append(needed_product)
    return result


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

    for needed_product in meat.needed_products:
        _needed_product = Needed_products(
            meat_id=_meat.id,
            weight=needed_product.weight,
            product_id=needed_product.product_id,
        )
        db.add(_needed_product)

    db.commit()
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

    db.commit()
    return
