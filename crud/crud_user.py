from fastapi import HTTPException, status

from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    db_user = models.User(
        username= user.username,
        password= user.password,
        role= user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user