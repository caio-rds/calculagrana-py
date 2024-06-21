import datetime
from typing import Optional

from beanie import Document
from pydantic import BaseModel


class TryLogin(Document):
    username: str
    password: str

    class Settings:
        name = 'users'
        validate_on_save = True


class Login(Document):
    username: str
    token: Optional[str]
    token_expire: datetime.datetime = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=10)
    logged_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    login_ip: str = 'Not Tracked'
    user_agent: str = 'Not Tracked'

    class Settings:
        name = 'logins'
        validate_on_save = True


class LoginResponse(BaseModel):
    username: str
    token: str
