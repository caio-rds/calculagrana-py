import datetime
from typing import Optional

from fastapi import HTTPException
import re
from beanie import Document, Indexed
from pydantic import BaseModel


from app.src.model.conversion import Conversion
from app.src.utils.validations import validate_password


class CreateUser(Document):
    username: Indexed(str, unique=True)
    email: Indexed(str, unique=True)
    password: str
    full_name: str
    phone_number: str
    created_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    updated_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)

    def __init__(self, **data):
        super().__init__(**data)
        try:
            validate_password(self.password)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        if re.search(r"\(\d{2}\)\s+\d{5}-\d{4}", self.phone_number) is None:
            raise HTTPException(status_code=400, detail="Invalid phone number format")
        if re.search(r'^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$', self.email) is None:
            raise HTTPException(status_code=400, detail="Invalid email format")
        if re.search(r"^[A-Za-záàâãéèêíìóòôõúùûüçÇ\-\s]+$", self.full_name) is None:
            raise HTTPException(status_code=400, detail="Invalid full name format")

    class Settings:
        name = 'users'
        validate_on_save = True


class ReadUser(Document):
    username: str
    email: str
    full_name: str
    phone_number: str
    conversions: list[Conversion] = []

    class Settings:
        name = 'users'
        validate_on_save = True


class UpdatedUser(Document):
    username: str
    email: str
    full_name: str
    phone_number: str
    updated_at: datetime.datetime

    class Settings:
        name = 'users'
        validate_on_save = True


class RequestUpdateUser(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    updated_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)

    def __init__(self, **data):
        super().__init__(**data)
        if self.phone_number and re.search(r"\(\d{2}\)\s+\d{5}-\d{4}", self.phone_number) is None:
            raise HTTPException(status_code=400, detail="Invalid phone number format")
        if self.email and re.search(r'^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$', self.email) is None:
            raise HTTPException(status_code=400, detail="Invalid email format")
        if self.full_name and re.search(r"^[A-Za-záàâãéèêíìóòôõúùûüçÇ\-\s]+$", self.full_name) is None:
            raise HTTPException(status_code=400, detail="Invalid full name format")


class UserDeleted(BaseModel):
    status: bool
    message: str
    username: str
    id: str


class RequestRecovery(BaseModel):
    username: str
    send_to: str


class ResponseRecovery(BaseModel):
    username: str
    code: str
    send_to: str
    request_date: datetime.datetime


class RecoveryByCode(BaseModel):
    username: str
    code: str
    new_password: str

    def __init__(self, **data):
        super().__init__(**data)
        try:
            validate_password(self.new_password)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))


class RecoveryByPassword(BaseModel):
    username: str
    password: str
    new_password: str

    def __init__(self, **data):
        super().__init__(**data)
        try:
            validate_password(self.new_password)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))


class Recovery(Document):
    username: str
    code: str
    way: str = 'email'
    send_to: str
    request_ip: str = 'Not Tracked'
    request_date: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    used: int = 0
    used_date: Optional[datetime.datetime] = None

    class Settings:
        name = 'recoveries'
        validate_on_save = True


class Recovered(BaseModel):
    status: bool
    message: str


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

