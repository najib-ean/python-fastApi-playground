from sqlmodel import Field, Relationship
from database.models.base import BaseModel


# table=True is a must
class Blog(BaseModel, table=True):
    __tablename__ = "blogs"

    title: str = Field(max_length=200)
    slug: str = Field(max_length=200, unique=True)
    content: str
    is_active: bool = Field(default=True)
    user_id: int = Field(default=None, foreign_key="users.id")

    # Relationship with User
    user: "User" = Relationship(back_populates="blogs")
