from pydantic import BaseModel, EmailStr, Field


class Credentials(BaseModel):
    email: EmailStr
    password: str = Field(
        ..., min_length=8, description="Password must be atleast 8 characters long."
    )
