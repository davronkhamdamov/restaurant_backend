from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session
from app.models import Orders
from app.schemas import Orders_schema


def get_orders(db: Session):
    return db.query(Orders).all()


def get_order_by_id(db: Session, order_id: UUID):
    return db.query(Orders).filter(Orders.id == order_id).first()


def create_order(db: Session, order: Orders_schema, staff_id: UUID):
    _orders = Orders(
        meat_id=order.meat_id,
        price=order.price,
        status=order.status,
        staff_id=staff_id,
        order_id=order.order_id,
        created_at=datetime.now(),
    )
    db.add(_orders)
    db.commit()
    db.refresh(_orders)
    return


def delete_order(db: Session, order_id: UUID):
    db.query(Orders).filter(Orders.id == order_id).delete()
    db.commit()
    return


def update_order(db: Session, order_id: UUID, order: Orders_schema):
    _order = get_order_by_id(db, order_id)
    _order.meat_id = order.meat_id
    _order.order_id = order.order_id
    _order.price = order.price
    _order.status = order.status,
    _order.updated_at = datetime.now()
    return
