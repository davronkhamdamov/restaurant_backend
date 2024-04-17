from datetime import datetime
from pydantic import BaseModel
from typing import Optional, TypeVar, Generic
from uuid import UUID

T = TypeVar("T")


class Login_schema(BaseModel):
    login: str
    password: str


class Response(BaseModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T] = None


class Staff_schema(BaseModel):
    id: str = None
    name: str
    surname: str
    login: str
    password: str
    role: str = None
    create_at: datetime = None
    updated_at: datetime = None


class Products_schema(BaseModel):
    id: UUID = None
    name: str
    price: str
    weight: str
    img_url: str
    created_at: str = None
    updated_at: str = None


class Products_weight_schema(BaseModel):
    weight: int


class Meats_schema(BaseModel):
    id: UUID = None
    name: str
    price: str
    img_url: str
    created_at: str = None
    updated_at: str = None


class Orders_schema(BaseModel):
    id: UUID
    order_id: str
    status: str
    price: str
    meat_id: UUID
    created_at: str = None
    updated_at: str = None


class Needed_product_schema(BaseModel):
    id: UUID = None
    product_id: UUID
    meat_id: UUID
    created_at: str = None
    updated_at: str = None
