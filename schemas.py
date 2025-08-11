import uuid
from typing import Optional

from models import UserRoleEnum

from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str
    password: str
    role: UserRoleEnum


class UserResponse(BaseModel):
    username: str


class User(BaseModel):
    id: uuid.UUID
    username: str
    role: UserRoleEnum

    class Config:
        from_attributes = True


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, alias="book_title")
    serial_number: str
    author: str


class BookResponse(BaseModel):
    title: str
    serial_number: str
    author: str
    user_id: Optional[uuid.UUID]


class BookAssign(BaseModel):
    serial_number: str

class BookRetrieveBySerialNumber(BookAssign):
    pass

class Book(BaseModel):
    title: str
    serial_number: str
    author: str
    user_id: Optional[uuid.UUID]

    class Config:
        from_attributes = True

User.model_rebuild()
