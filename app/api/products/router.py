from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.db import get_db
from app.schemas import Response, Products_schema
from app.utils.auth_middleware import get_current_staff
from app.api.products.crud import (
    get_product_by_id,
    get_products,
    create_product,
    delete_product,
    update_product,
)

router = APIRouter()


@router.get("/{product_id}")
async def get_product_by_id_route(
    product_id: UUID,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    _product = get_product_by_id(db, product_id)
    return Response(
        code=200, status="ok", message="success", result=_product
    ).model_dump()


@router.get("/")
def get_all_products_route(db: Session = Depends(get_db), _=Depends(get_current_staff)):
    _products = get_products(db)


@router.post("/")
def create_product_route(
    product: Products_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    create_product(db, product)
    return Response(code=201, status="ok", message="created").model_dump()


()


@router.delete("/")
def delete_product_rout(
    product_id: UUID, db: Session = Depends(get_db), _=Depends(get_current_staff)
):
    delete_product(db, product_id)
    return Response(code=200, status="ok", message="deleted")


@router.put("/{product_id}")
def update_product_rout(
    product_id: UUID,
    product: Products_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    update_product(db, product_id, product)
    return Response(code=200, status="ok", message="updated")
