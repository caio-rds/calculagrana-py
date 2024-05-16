from fastapi import HTTPException

import re

from pydantic import BaseModel
from typing import Optional

from app.src.services.auth import pwd_hash


class CreateUser(BaseModel):
    username: str
    email: str
    password: str
    full_name: str
    phone_number: str

    def __init__(self, **data):
        super().__init__(**data)
        if re.search(r"\(\d{2}\)\s+\d{5}-\d{4}", self.phone_number) is None:
            raise HTTPException(status_code=400, detail="Invalid phone number format")
        if re.search(r'^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$', self.email) is None:
            raise HTTPException(status_code=400, detail="Invalid email format")
        self.validate_pwd()
        if re.search(r"^[A-Za-záàâãéèêíìóòôõúùûüçÇ\-\s]+$", self.full_name) is None:
            raise HTTPException(status_code=400, detail="Invalid full name format")

    def validate_pwd(self):
        upper = False
        lower = False
        number = False
        special = False
        for char in self.password:
            if char.isupper():
                upper = True
            if char.islower():
                lower = True
            if char.isdigit():
                number = True
            if char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";",
                        ":", "'", '"', "<", ">", ",", ".", "?", "/"]:
                special = True
        if not upper:
            raise HTTPException(status_code=400, detail="Password must contain at least one uppercase letter")
        if not lower:
            raise HTTPException(status_code=400, detail="Password must contain at least one lowercase letter")
        if not number:
            raise HTTPException(status_code=400, detail="Password must contain at least one number")
        if not special:
            raise HTTPException(status_code=400, detail="Password must contain at least one special character")
        if len(self.password) < 8:
            raise HTTPException(status_code=400, detail="Password must contain at least 8 characters")


class ReadUser(BaseModel):
    email: str
    username: str
    full_name: str
    phone_number: str
    conversions: Optional[list] = None


class UpdateUser(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    phone_number: Optional[str] = None


class UpdateUserPassword(BaseModel):
    username: str
    password: str
