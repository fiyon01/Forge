from enum import Enum
from pydantic import BaseModel, EmailStr, Field


class userRole(str, Enum):
    mentor = "mentor"
    mentee = "mentee"


class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: userRole
    phone_number: str | None = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)