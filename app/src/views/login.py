from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm

# from app.src.controller.login import match_user, upsert_token
from app.src.utils.auth import auth_wrapper

router = APIRouter()


@router.get("/")
async def login(username=Depends(auth_wrapper)) -> dict:
    if username.get('successful'):
        return {"username": username.get('username')}


@router.post("/")
async def try_login(request: Request, form: OAuth2PasswordRequestForm = Depends()) -> dict:
    pass
    # if await match_user(form.username, form.password, request.client.host, request.headers.get('User-Agent')):
    #     return {"token": await upsert_token(form.username)}
    # raise HTTPException(status_code=401, detail="Invalid credentials")
