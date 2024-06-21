from http.client import HTTPException

from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

from app.src.controller.login import match_user
from app.src.models.login import LoginResponse

from app.src.utils.auth import auth_wrapper

router = APIRouter()


@router.get("/")
async def login(username=Depends(auth_wrapper)) -> dict:
    if username.get('successful'):
        return {"username": username.get('username')}
    raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/")
async def try_login(request: Request, form: OAuth2PasswordRequestForm = Depends()) -> LoginResponse:
    if user := await match_user(form.username, form.password, request.client.host, request.headers.get('User-Agent')):
        return user
