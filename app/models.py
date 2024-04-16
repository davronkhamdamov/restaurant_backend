import datetime
import uuid

from sqlalchemy import Column, String, DateTime, UUID, ForeignKey, Integer

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


class Products(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    price = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)


class Meats(Base):
    __tablename__ = "meats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)


class Orders(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(Integer, autoincrement=True)
    status = Column(String, default="Kutilmoqda")
    price = Column(Integer, nullable=False)
    staff_id = Column(UUID, ForeignKey("staffs.id"))
    meat_id = Column(UUID, ForeignKey("meats.id"))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)


class Needed_products(Base):
    __tablename__ = "needed_products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID, ForeignKey("products.id"))
    meat_id = Column(UUID, ForeignKey("meats.id"))
    weight = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)


# Base.metadata.create_all(bin(engine))
