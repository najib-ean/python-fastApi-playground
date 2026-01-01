from typing import List
from database.models.base import BaseModel
from sqlmodel import Field, Relationship


# table=True is a must
class User(BaseModel, table=True):
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    full_name: str
    password: str

    blog: List("Blog") = Relationship(back_populates="user")
