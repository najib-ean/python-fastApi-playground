from sqlmodel import Session
from fastapi import Depends
from database.models.user import User
from schemas.user import UserSchema
from database.db import get_db


def create_user_controller(user: UserSchema, db: Session = Depends(get_db)) -> User:
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        password=user.password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
