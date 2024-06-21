import datetime
from typing import Optional
from beanie import Document, Indexed
from pydantic import BaseModel


class ResultConversion(BaseModel):
    code: str
    value: float
    last_update: datetime.datetime


class Conversion(Document):
    base_currency: str
    to_currency: list[str] | str
    amount: float
    username: Indexed(str)
    conversions: list[ResultConversion] = []
    user_agent: Optional[str] = None
    request_ip: str
    request_date: Optional[datetime.datetime] = datetime.datetime.now()

    class Settings:
        name = 'conversions'


class ConversionRequest(BaseModel):
    base_currency: Optional[str] = 'EUR'
    to_currency: list[str] | str
    amount: float
    username: Optional[str] = 'Anonymous'
    request_ip: Optional[str] = 'Not Tracked'
    user_agent: Optional[str] = None


class Currency(Document):
    code: Indexed(str, unique=True)
    name: str
    name_plural: str
    value: float
    base_currency: str
    updated_at: datetime.datetime = datetime.datetime.now()

    class Settings:
        name = 'currencies'
