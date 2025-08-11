from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

import crud.crud_user
import models
import schemas
from database import get_db
from schemas import User

user_api = APIRouter()

def get_current_user_role(user_id: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user.role == "admin":
        return True
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

@user_api.post(
    "/create_user",
    response_model=User,
    summary= "create user",
    description="API to create user"
)
def create_user(
        user_to_create: schemas.UserCreate,
        db: Session = Depends(get_db)
):
    new_user = crud.crud_user.create_user(db=db, user=user_to_create)

    return new_user

@user_api.get(
    "/{username}",
    response_model=User,
    summary="get user by username",
    description="API to get user by username"
)
def get_user_by_username(
    username: str,
    db: Session = Depends(get_db)
):
    user = crud.crud_user.get_user_by_username(db=db, username=username)

    return user