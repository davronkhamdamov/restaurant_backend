from datetime import datetime
from pydantic import BaseModel
from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class Login_schema(BaseModel):
    login: str
    password: str


class Response(BaseModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T]


class Staff_schema(BaseModel):
    id: str = None
    name: str
    surname: str
    login: str
    password: str
    role: str = None
    create_at: datetime = None
    updated_at: datetime = None


class Products(BaseModel):
    id: str = None
    name: str
    price: str
    weight: str
    created_at: str = None
    updated_at: str = None


class Meats(BaseModel):
    id: str
    name: str
    price: str
    created_at: str = None
    updated_at: str = None


class Orders(BaseModel):
    id: str
    order_id: str
    status: str
    price: str
    meat_id: str
    created_at: str = None
    updated_at: str = None


class Needed_products(BaseModel):
    id: str
    product_id: str
    meat_id: str
    created_at: str = None
    updated_at: str = None
