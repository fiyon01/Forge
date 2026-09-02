from fastapi import APIRouter, status
from controllers.auth import create_user, login_user
from schemas.auth import SignupRequest, LoginRequest


router = APIRouter(
    prefix="/api/v1",
    tags=["auth"]
)

@router.post("/auth/signup", status_code=status.HTTP_201_CREATED)
def signup_user(payload: SignupRequest):
    result = create_user(payload)
    return {"message": "User created successfully", "data": result}

@router.post("/auth/login",status_code=status.HTTP_200_OK)
def signin_user(payload: LoginRequest):
    result = login_user(payload)
    return {"message": "Login successful", "data": result}

