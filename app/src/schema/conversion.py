from app.src.services.database import Base
from sqlalchemy import Column, String, Integer, DateTime, JSON
import datetime


class Conversion(Base):
    __tablename__ = "conversions"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    base_currency = Column(String)
    amount = Column(Integer)
    conversions = Column(JSON)
    username = Column(String, index=True, default='anonymous')
    request_ip = Column(String)
    conversion_id = Column(String, index=True, unique=True)
    request_date = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    def __repr__(self):
        return (f"Conversion(base_currency={self.base_currency}, amount={self.amount}, conversions={self.conversions},"
                f" username={self.username}, request_ip={self.request_ip}, conversion_id={self.conversion_id},"
                f" request_date={self.request_date}")


class Currencies(Base):
    __tablename__ = "currencies"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    code = Column(String, index=True, unique=True)
    name = Column(String)
    name_plural = Column(String)
    value = Column(Integer)
    base_currency = Column(String)
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    def __repr__(self):
        return (f"Currencies(code={self.code}, name={self.name}, name_plural={self.name_plural},"
                f" value={self.value}, base_currency={self.base_currency}, updated_at={self.updated_at}")
