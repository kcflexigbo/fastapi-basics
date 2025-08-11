import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
from database import get_db
from crud import crud_book

router = APIRouter()


@router.post(
    "/create_book",
    response_model=schemas.BookResponse,
    summary="Create a Book",
    description="API to create a book"
)
def create_book(
        book_to_create: schemas.BookCreate,
        db: Session = Depends(get_db),
):
    book = crud_book.create_book(db=db, book_to_create=book_to_create)

    return book

@router.post(
    "/{user_id}/assign",
    response_model=schemas.BookResponse,
    summary="Assign a Book",
    description="API to assign a book to a user"
)
def assign_book(
    user_id : uuid.UUID,
    book_to_assign : schemas.BookAssign,
    db: Session = Depends(get_db)
):
    book = crud_book.assign_book(db= db, user_id = user_id, book_to_assign = book_to_assign)

    return book

@router.get(
    "/{book_serial_number}",
    response_model=Optional[schemas.BookResponse],
    summary="Retrieve a Book",
    description="API to retrieve a book by serial number"
)
def get_book_by_serial_number(
    book_serial_number : str,
    db: Session = Depends(get_db)
):
    book = crud_book.get_book_by_serial_number(db= db, book_serial_number = book_serial_number)

    return book