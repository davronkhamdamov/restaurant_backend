from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from app.db import get_db
from app.schemas import Response, Staff_schema
from app.utils.auth_middleware import get_current_staff
from app.api.staffs.crud import (
    get_staff_by_id,
    get_staffs,
    create_staff,
    delete_staff,
    update_staff,
)

router = APIRouter()


@router.get("/{staff_id}")
async def get_staff_by_id_route(
    staff_id: UUID,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    _staff = get_staff_by_id(db, staff_id)
    return Response(
        code=200, status="ok", message="success", result=_staff
    ).model_dump()


@router.get("/")
def get_all_staffs_route(db: Session = Depends(get_db), _=Depends(get_current_staff)):
    _staffs = get_staffs(db)


@router.post("/")
def create_staff_route(
    staff: Staff_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    create_staff(db, staff)
    return Response(code=201, status="ok", message="created").model_dump()


()


@router.delete("/")
def delete_staff_rout(
    staff_id: UUID, db: Session = Depends(get_db), _=Depends(get_current_staff)
):
    delete_staff(db, staff_id)
    return Response(code=200, status="ok", message="deleted")


@router.put("/{staff_id}")
def update_staff_rout(
    staff_id: UUID,
    staff: Staff_schema,
    db: Session = Depends(get_db),
    _=Depends(get_current_staff),
):
    update_staff(db, staff_id, staff)
    return Response(code=200, status="ok", message="updated")
