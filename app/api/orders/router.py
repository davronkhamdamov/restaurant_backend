from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db import get_db
from app.schemas import Response, Orders_schema
from app.utils.auth_middleware import get_current_staff
from app.api.orders.crud import (
    get_order_by_id,
    get_orders,
    create_order,
    delete_order,
    update_order,
)
from app.api.meat.crud import get_meat_by_id

router = APIRouter()


@router.get("/{order_id}")
async def get_order_by_id_route(
    order_id: UUID,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    _order = get_order_by_id(db, order_id)
    return Response(
        code=200, status="ok", message="success", result=_order
    ).model_dump()


@router.get("/")
def get_all_orders_route(db: Session = Depends(get_db), _=Depends(get_current_staff)):
    _orders = get_orders(db)


@router.post("/")
def create_order_route(
    order: Orders_schema,
    db: Session = Depends(get_db),
    current_staff: dict = Depends(get_current_staff),
):
    _meat = get_meat_by_id(db, order.meat_id)
    if not _meat:
        return HTTPException(status_code=404, detail="Meat not found")
    create_order(db, order, staff_id=current_staff["id"])
    return Response(code=201, status="ok", message="created").model_dump()


@router.delete("/")
def delete_order_rout(
    order_id: UUID, db: Session = Depends(get_db), _=Depends(get_current_staff)
):
    delete_order(db, order_id)
    return Response(code=200, status="ok", message="deleted")


@router.put("/{order_id}")
def update_order_rout(
    order_id: UUID,
    order: Orders_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    update_order(db, order_id, order)
    return Response(code=200, status="ok", message="updated")
