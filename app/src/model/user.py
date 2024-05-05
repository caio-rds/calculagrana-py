from pydantic import BaseModel
from typing import Optional

from app.src.services.auth import pwd_hash


class CreateUser(BaseModel):
    username: str
    email: str
    password: str


class ReadUser(BaseModel):
    email: str
    username: str
    full_name: Optional[str] = None


class UpdateUser(BaseModel):
    username: str
    email: Optional[str] = None
    password: Optional[str] = None
