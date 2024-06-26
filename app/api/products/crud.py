from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session
from app.models import Products
from app.schemas import Products_schema, Products_weight_schema


def get_products(db: Session):
    return db.query(Products).all()


def get_product_by_id(db: Session, product_id: UUID):
    return db.query(Products).filter(Products.id == product_id).first()


def create_product(db: Session, product: Products_schema):
    _product = Products(
        name=product.name,
        price=product.price,
        img_url=product.img_url,
        weight=product.weight,
        weight_type=product.weight_type,
        created_at=datetime.now(),
    )
    db.add(_product)
    db.commit()
    db.refresh(_product)
    return


def delete_product(db: Session, product_id: UUID):
    db.query(Products).filter(Products.id == product_id).delete()
    db.commit()
    return


def update_product(db: Session, product_id: UUID, product: Products_schema):
    _product = get_product_by_id(db, product_id)
    _product.name = product.name
    _product.price = product.price
    _product.weight = product.weight
    _product.weight_type = product.weight_type
    _product.updated_at = datetime.now()
    db.commit()
    return


def update_product_weight(db: Session, product_id: UUID, product_weight: int):
    _product = get_product_by_id(db, product_id)
    _product.weight += product_weight
    _product.updated_at = datetime.now()
    db.commit()
    return


def update_product_weight_for_order(db: Session, product_id: UUID, product_weight: int):
    _product = get_product_by_id(db, product_id)
    _product.weight = product_weight
    _product.updated_at = datetime.now()
    return
