from controllers.user import create_user_controller
from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database.db import get_db
from schemas.user import UserSchema
from database.models.user import User

router = APIRouter()


@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema, db: Session = Depends(get_db)) -> User:
    return create_user_controller(user, db)
