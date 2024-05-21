import datetime

from pydantic import BaseModel
from typing import Optional


class Conversion(BaseModel):
    base_currency: Optional[str] = 'EUR'
    to_currency: list[str] | str
    amount: float
    conversions: Optional[dict] = {}
    username: Optional[str] = 'anonymous'
    request_ip: Optional[str] = None
    conversion_id: str = None
    request_date: Optional[datetime.datetime] = datetime.datetime.now()


class Currencies(BaseModel):
    code: str
    name: str
    name_plural: str
