from controllers.auth_controller import login_controller, signup_controller
from fastapi import APIRouter, status
from helpers.api_paths import ApiPaths
from models.credentials import Credentials

router = APIRouter()


@router.post(ApiPaths.AUTH_SIGNUP, status_code=status.HTTP_201_CREATED)
async def signup(payload: Credentials):
    return await signup_controller(email=payload.email, password=payload.password)


@router.post(ApiPaths.AUTH_LOGIN, status_code=status.HTTP_200_OK)
async def login(payload: Credentials):
    return await login_controller(email=payload.email, password=payload.password)
