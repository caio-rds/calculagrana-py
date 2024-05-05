from app.src.services.database import Base
from sqlalchemy import Column, String, Integer, DateTime
import datetime


class User(Base):
    __tablename__ = "users"
    username = Column(String, unique=True, index=True, primary_key=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    token = Column(String)
    login_at = Column(Integer, default=0)
    recovery_code = Column(String)

    def __repr__(self):
        return f"<User {self.username}>"
