from datetime import datetime
from typing import List
from uuid import UUID

from sqlalchemy.orm import Session
from app.models import Orders, Meats
from app.schemas import Orders_schema


def get_orders(db: Session, staff_id: UUID):
    return (
        db.query(Orders, Meats)
        .join(Meats, Orders.meat_id == Meats.id)
        .filter(Orders.staff_id == staff_id)
        .filter(Orders.status != "Tugatildi")
        .order_by(Orders.updated_at.desc())
        .all()
    )


def get_order_by_id(db: Session, order_id: UUID):
    return db.query(Orders).filter(Orders.id == order_id).first()


def create_order(db: Session, orders: List[Orders_schema], staff_id: UUID):
    for order in orders:
        _order = Orders(
            meat_id=order.meat_id,
            price=order.price * order.count,
            staff_id=staff_id,
            count=order.count,
            created_at=datetime.now(),
        )
        db.add(_order)
    return


def delete_order(db: Session, order_id: UUID):
    db.query(Orders).filter(Orders.id == order_id).delete()
    db.commit()
    return


def update_order(db: Session, order_id: UUID, order: Orders_schema):
    _order = get_order_by_id(db, order_id)
    _order.status = (order.status,)
    _order.updated_at = datetime.now()
    db.commit()
    return
