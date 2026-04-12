from sqlmodel import Session
from fastapi import Depends
from database.models.user import User
from schemas.user import UserSchema
from database.db import get_db
from dto.user_dto import *


def create_user_controller(user_data: CreateUserSchema, db: Session) -> User:
    user = User(
        username=user_data.username,
        email=user_data.email,
        full_name=user_data.full_name,
        password=user_data.password,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_controller(db: Session):
    return db.query(User).all()


def get_user_by_id_controller(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def update_user_controller(user_id: int, user_data: UpdateUserSchema, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user
