from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session
from app.models import Needed_products
from app.schemas import Needed_product_schema


def get_needed_products(db: Session):
    return db.query(Needed_products).all()


def get_needed_product_by_id(db: Session, needed_product_id: UUID):
    return (
        db.query(Needed_products)
        .filter(Needed_products.id == needed_product_id)
        .first()
    )


def create_needed_product(db: Session, needed_product: Needed_product_schema):
    _needed_products = Needed_products(
        product_id=needed_product.meat_id,
        meat_id=needed_product.meat_id,
        weight=needed_product.weight,
        created_at=datetime.now(),
    )
    db.add(_needed_products)
    db.commit()
    db.refresh(_needed_products)
    return


def delete_needed_product(db: Session, needed_product_id: UUID):
    db.query(Needed_products).filter(Needed_products.id == needed_product_id).delete()
    db.commit()
    return


def update_needed_product(
    db: Session, needed_product_id: UUID, needed_product: Needed_product_schema
):
    _needed_product = get_needed_product_by_id(db, needed_product_id)
    _needed_product.product_id = needed_product.product_id
    _needed_product.meat_id = needed_product.meat_id
    _needed_product.updated_at = datetime.now()
    return
