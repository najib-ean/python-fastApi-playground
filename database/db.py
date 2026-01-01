from sqlmodel import create_engine, Session, SQLModel
from core.config import settings

print(f"DATABASE_URL is {settings.DATABASE_URL}")

engine = create_engine(settings.DATABASE_URL)


# ⬇️ Import ALL models here so they register with SQLModel.metadata
from database.models.user import User
from database.models.blog import Blog


# ⬇️ Now create tables (only once at app startup)
def init_db():
    print("Creating tables")
    SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
