import datetime

from app.src.models.login import Login, LoginResponse, TryLogin
from app.src.utils.auth import check_pwd, encode_token
from app.src.utils.custom_exceptions import NotFound, PasswordMismatch, UserNotFound


# async def upsert_token(username: str) -> str:
#     if user := await Login.find_one(Login.username == username):
#         if user.token_expire < datetime.datetime.now(datetime.timezone.utc):
#             return user.token
#         user.token = await encode_token(username)
#         user.token_expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)
#         await user.save()
#         return user.token
#     raise UserNotFound


async def match_user(username: str, password: str, login_ip: str, user_agent: str) -> LoginResponse:
    if user := await TryLogin.find_one(TryLogin.username == username):
        if await check_pwd(password, user.password):
            login = Login(
                username=user.username,
                token=await encode_token(username),
                login_ip=login_ip,
                user_agent=user_agent
            )
            await login.save()
            return LoginResponse(
                username=login.username,
                token=login.token
            )
        raise PasswordMismatch
    raise UserNotFound
