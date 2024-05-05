from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.src.controller.login import match_user, upsert_token
from app.src.services.auth import auth_wrapper

router = APIRouter()


@router.get("/")
async def login(username=Depends(auth_wrapper)) -> dict:
    if username.get('successful'):
        return {"username": username.get('username')}


@router.post("/")
async def try_login(form: OAuth2PasswordRequestForm = Depends()) -> dict:
    if await match_user(form.username, form.password):
        return {"token": await upsert_token(form.username)}
    raise HTTPException(status_code=401, detail="Invalid credentials")
