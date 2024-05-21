from app.src.services.database import Base
from sqlalchemy import Column, String, Integer, DateTime, VARCHAR
import datetime


class User(Base):
    __tablename__ = "users"
    username = Column(String, unique=True, index=True, primary_key=True)
    password = Column(String)
    email = Column(VARCHAR, unique=True, index=True)
    full_name = Column(VARCHAR)
    phone_number = Column(VARCHAR)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    token = Column(String)

    def __repr__(self):
        return f"<User {self.username}>"


class UserLogin(Base):
    __tablename__ = "logins"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    logged_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    login_ip = Column(String)
    user_agent = Column(String)

    def __repr__(self):
        return f"<User {self.username}>"


class Recovery(Base):
    __tablename__ = "recovery"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    code = Column(String, index=True)
    way = Column(String, default="email")
    send_to = Column(String)
    request_ip = Column(String)
    request_date = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    used = Column(Integer, default=0)
    used_date = Column(DateTime, default=None)

    def __repr__(self):
        return f"<Recovery {self.username}>"

