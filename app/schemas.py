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
