from app.src.services.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Date
import datetime


class Conversion(Base):
    __tablename__ = "conversions"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    from_currency = Column(String)
    to_currency = Column(String)
    amount = Column(Integer)
    conversion_value = Column(Integer)
    username = Column(String, index=True, default='anonymous')
    request_ip = Column(String)
    conversion_id = Column(String, index=True, unique=True)
    request_date = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    def __repr__(self):
        return (f"Conversion(from_currency={self.from_currency}, to_currency={self.to_currency}, amount={self.amount},"
                f"conversion_value={self.conversion_value}, username={self.username}, request_ip={self.request_ip},"
                f"conversion_id={self.conversion_id}, request_date={self.request_date}")
