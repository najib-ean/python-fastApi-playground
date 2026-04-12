from controllers.user import *
from sqlmodel import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database.db import get_db
from schemas.user import UserSchema
from database.models.user import User
from dto.user_dto import *

router = APIRouter()


@router.post(
    "/users",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: CreateUserSchema, db: Session = Depends(get_db)) -> User:
    return create_user_controller(user, db)


@router.get(
    "/users", response_model=list[UserResponseSchema], status_code=status.HTTP_200_OK
)
def get_users(db: Session = Depends(get_db)) -> list[User]:
    return get_user_controller(db)


@router.get(
    "/users/{user_id}",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
)
def get_users(user_id: int, db: Session = Depends(get_db)) -> User:
    user = get_user_by_id_controller(user_id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


@router.patch(
    "/users/{user_id}",
    response_model=UserResponseSchema,
    status_code=status.HTTP_200_OK,
)
def get_users(
    user_id: int, user: UpdateUserSchema, db: Session = Depends(get_db)
) -> User:
    updated_user = update_user_controller(user_id, user, db)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return updated_user


@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_users(user_id: int, db: Session = Depends(get_db)):
    user = delete_user_controller(user_id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return {"message": "User deleted successfully."}
