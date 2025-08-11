import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas


def create_book(db: Session, book_to_create: schemas.BookCreate):
    book = db.query(models.Books).filter(models.Books.serial_number == book_to_create.serial_number).first()
    if book:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book already exists")

    book = models.Books(
        **book_to_create.model_dump()
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def assign_book(db: Session, user_id: uuid.UUID, book_to_assign: schemas.BookAssign):
    book = db.query(models.Books).filter(models.Books.serial_number == book_to_assign.serial_number).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book not found")

    if book.user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book already assigned")

    if book.user_id == user_id:
        return book

    book.user_id = user_id
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_book_by_serial_number(db: Session, book_serial_number: str):
    book = db.query(models.Books).filter(models.Books.serial_number == book_serial_number).first()
    if not book:
        return None

    return book