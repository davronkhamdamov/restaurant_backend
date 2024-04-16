import hashlib
from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import Session
from app.models import Staffs
from app.schemas import Staff_schema


def get_staffs(db: Session):
    return db.query(Staffs).all()


def get_staff_by_id(db: Session, staff_id: UUID):
    return db.query(Staffs).filter(Staffs.id == staff_id).first()


def create_staff(db: Session, staff: Staff_schema):
    _staff = Staffs(
        name=staff.name,
        surname=staff.surname,
        login=staff.login,
        password=hashlib.sha256(staff.password.encode()).hexdigest(),
        role=staff.role,
    )
    db.add(_staff)
    db.commit()
    db.refresh(_staff)
    return


def delete_staff(db: Session, staff_id: UUID):
    db.query(Staffs).filter(Staffs.id == staff_id).delete()
    db.commit()
    return


def update_staff(db: Session, staff_id: UUID, staff: Staff_schema):
    _staff = get_staff_by_id(db, staff_id)
    _staff.name = staff.name
    _staff.surname = staff.surname
    _staff.login = staff.login
    _staff.password = staff.password
    _staff.role = staff.role
    _staff.updated_at = datetime.now()
