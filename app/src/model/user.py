import datetime
from typing import Optional

from fastapi import HTTPException
import re
from beanie import Document, Indexed
from pydantic import BaseModel


from app.src.model.conversion import Conversion


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
        if re.search(r"\(\d{2}\)\s+\d{5}-\d{4}", self.phone_number) is None:
            raise HTTPException(status_code=400, detail="Invalid phone number format")
        if re.search(r'^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$', self.email) is None:
            raise HTTPException(status_code=400, detail="Invalid email format")
        self.validate_pwd()
        if re.search(r"^[A-Za-záàâãéèêíìóòôõúùûüçÇ\-\s]+$", self.full_name) is None:
            raise HTTPException(status_code=400, detail="Invalid full name format")

    def validate_pwd(self):
        upper = False
        lower = False
        number = False
        special = False
        for char in self.password:
            if char.isupper():
                upper = True
            if char.islower():
                lower = True
            if char.isdigit():
                number = True
            if char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";",
                        ":", "'", '"', "<", ">", ",", ".", "?", "/"]:
                special = True
        if not upper:
            raise HTTPException(status_code=400, detail="Password must contain at least one uppercase letter")
        if not lower:
            raise HTTPException(status_code=400, detail="Password must contain at least one lowercase letter")
        if not number:
            raise HTTPException(status_code=400, detail="Password must contain at least one number")
        if not special:
            raise HTTPException(status_code=400, detail="Password must contain at least one special character")
        if len(self.password) < 8:
            raise HTTPException(status_code=400, detail="Password must contain at least 8 characters")

    class Settings:
        name = 'users'


class ReadUser(Document):
    username: str
    email: str
    full_name: str
    phone_number: str
    conversions: list[Conversion] = []

    class Settings:
        name = 'users'


class UpdatedUser(Document):
    username: str
    email: str
    full_name: str
    phone_number: str
    updated_at: datetime.datetime

    class Settings:
        name = 'users'


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


# class RequestRecovery(Document):
#     username: str
#     send_to: str
#
#
# class ResponseRecovery(Document):
#     username: str
#     code: str
#     send_to: str
#     request_ip: str
#     request_date: datetime.datetime
#
#
# class RecoveryByCode(Document):
#     username: str
#     code: str
#     new_password: str
#
#
# class RecoveryByPassword(Document):
#     username: str
#     password: str
#     new_password: str
#
#
# class Recovery(Document):
#     username: str
#     code: str
#     way: str = 'email'
#     send_to: str
#     request_ip: str = 'Not Tracked'
#     request_date: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
#     used: int = 0
#     used_date: Optional[datetime.datetime] = None
#
#

class Login(Document):
    username: str
    logged_at: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
    login_ip: str = 'Not Tracked'
    user_agent: str = 'Not Tracked'

    class Settings:
        name = 'users'
