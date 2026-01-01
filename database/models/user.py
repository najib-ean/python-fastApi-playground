from typing import List
from database.models.base import BaseModel
from sqlmodel import Field, Relationship


# table=True is a must
class User(BaseModel, table=True):
    __tablename__ = "users"

    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    full_name: str
    password: str

    # Relationship with Blog
    blogs: List["Blog"] = Relationship(back_populates="user")
