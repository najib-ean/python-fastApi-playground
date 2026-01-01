from pydantic import BaseModel, Field, field_validator


class UserCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=255)
    email: str = Field(..., min_length=5, max_length=255)
    password: str = Field(..., min_length=8, max_length=20)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Email must contain @")
        return v
