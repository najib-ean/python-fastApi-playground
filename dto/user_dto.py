from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class BaseUserSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None


class CreateUserSchema(BaseUserSchema):
    username: str
    email: str
    full_name: str
    password: str


# Do not inherite from BaseUserSchema to get the order JSON correctly; presented like below.
class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    created_at: datetime
    updated_at: datetime

    # model_config = {"from_attributes": True}


class UpdateUserSchema(BaseUserSchema):
    pass
