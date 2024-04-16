from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.db import get_db
from app.schemas import Response, Meats_schema
from app.utils.auth_middleware import get_current_staff
from app.api.meat.crud import (
    get_meat_by_id,
    get_meats,
    create_meat,
    delete_meat,
    update_meat,
)

router = APIRouter()


@router.get("/{meat_id}")
async def get_meat_by_id_route(
    meat_id: UUID,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    _meat = get_meat_by_id(db, meat_id)
    return Response(code=200, status="ok", message="success", result=_meat).model_dump()


@router.get("/")
def get_all_meats_route(db: Session = Depends(get_db), _=Depends(get_current_staff)):
    _meats = get_meats(db)


@router.post("/")
def create_meat_route(
    meat: Meats_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    create_meat(db, meat)
    return Response(code=201, status="ok", message="created").model_dump()


@router.delete("/")
def delete_meat_rout(
    meat_id: UUID, db: Session = Depends(get_db), _=Depends(get_current_staff)
):
    delete_meat(db, meat_id)
    return Response(code=200, status="ok", message="deleted")


@router.put("/{meat_id}")
def update_meat_rout(
    meat_id: UUID,
    meat: Meats_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    update_meat(db, meat_id, meat)
    return Response(code=200, status="ok", message="updated")
