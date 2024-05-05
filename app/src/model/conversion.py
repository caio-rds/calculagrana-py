from pydantic import BaseModel
from typing import Optional


class Conversion(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    conversion_value: Optional[float] = None
    username: Optional[str] = None
    request_ip: Optional[str] = None
    conversion_id: str = None
    request_date: str = None

