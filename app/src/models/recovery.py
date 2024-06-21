from typing import Optional

from beanie import Document
from fastapi import HTTPException
from pydantic import BaseModel
import datetime

from app.src.utils.validations import validate_password


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
