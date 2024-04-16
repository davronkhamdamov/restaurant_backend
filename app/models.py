import datetime
import uuid

from sqlalchemy import Column, String, DateTime, UUID, ForeignKey, Boolean

from app.db import Base, engine


class Staffs(Base):
    __tablename__ = "staffs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    surname = Column(String, index=True, nullable=False)
    login = Column(String, nullable=True)
    password = Column(String, nullable=True)
    role = Column(String, default="staff")
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)


# Base.metadata.create_all(bin(engine))
