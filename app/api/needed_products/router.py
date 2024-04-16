from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db import get_db
from app.schemas import Response, Needed_product_schema
from app.utils.auth_middleware import get_current_staff
from app.api.needed_products.crud import (
    get_needed_product_by_id,
    get_needed_products,
    create_needed_product,
    delete_needed_product,
    update_needed_product,
)
from app.api.meat.crud import get_meat_by_id

router = APIRouter()


@router.get("/{needed_product_id}")
async def get_needed_product_by_id_route(
    needed_product_id: UUID,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    _needed_product = get_needed_product_by_id(db, needed_product_id)
    return Response(
        code=200, status="ok", message="success", result=_needed_product
    ).model_dump()


@router.get("/")
def get_all_needed_products_route(
    db: Session = Depends(get_db), _=Depends(get_current_staff)
):
    _needed_products = get_needed_products(db)


@router.post("/")
def create_needed_product_route(
    needed_product: Needed_product_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    _meat = get_meat_by_id(db, needed_product.meat_id)
    if not _meat:
        return HTTPException(status_code=404, detail="Meat not found")
    _product = get_meat_by_id(db, needed_product.product_id)
    if not _product:
        return HTTPException(status_code=404, detail="Product not found")
    create_needed_product(db, needed_product)
    return Response(code=201, status="ok", message="created").model_dump()


@router.delete("/")
def delete_needed_product_rout(
    needed_product_id: UUID, db: Session = Depends(get_db), _=Depends(get_current_staff)
):
    delete_needed_product(db, needed_product_id)
    return Response(code=200, status="ok", message="deleted")


@router.put("/{needed_product_id}")
def update_needed_product_rout(
    needed_product_id: UUID,
    needed_product: Needed_product_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    update_needed_product(db, needed_product_id, needed_product)
    return Response(code=200, status="ok", message="updated")
