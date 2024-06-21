import datetime
from typing import Optional

from fastapi import HTTPException
import re
from beanie import Document, Indexed
from pydantic import BaseModel


from app.src.models.conversion import Conversion
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


class TryUpdateUsername(Document):
    username: str

    class Settings:
        name = 'users'


class RequestUpdateUsername(BaseModel):
    username: str
    new_username: str


class ResponseUpdateUsername(BaseModel):
    status: bool
    message: str
    username: str
    new_username: str


class UserDeleted(BaseModel):
    status: bool
    message: str
    username: str
    id: str
