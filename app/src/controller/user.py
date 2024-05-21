from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.src.model.user import CreateUser, ReadUser, UpdateUser
from app.src.schema.conversion import Conversion
from app.src.services.database import *
from app.src.services.auth import pwd_hash
from app.src.schema.user import User
from sqlalchemy.orm import Session

# from app.src.services.logs import create_log

db: Session = SessionLocal()


async def read(username: str, conversions: bool = False) -> dict | None:
    result = {}
    if user := db.query(User).filter(User.username == username).first():
        result.update({
            'email': user.email,
            'username': user.username,
            'full_name': user.full_name,
            'phone_number': user.phone_number
        })
        if conversions:
            user_conversions = db.query(Conversion).filter(Conversion.username == user.username).all()
            result.update({'conversions': [jsonable_encoder(c) for c in user_conversions]})
    db.close()
    return result


async def create(new_user: CreateUser) -> dict:
    new_user.password = await pwd_hash(new_user.password)
    user = User(**new_user.dict())
    if db.query(User).filter(User.email == new_user.email or User.username == new_user.username).first():
        db.close()
        raise ValueError('User already exists')
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return {
        'email': user.email,
        'username': user.username,
        'full_name': user.full_name,
        'phone_number': user.phone_number
    }


async def update(user_update: UpdateUser) -> dict:
    if user := db.query(User).filter(User.username == user_update.username).first():
        for key, value in user_update.dict(exclude_unset=True).items():
            if value == getattr(user, key):
                continue
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        db.close()
        return {
            'email': user.email,
            'username': user.username,
            'full_name': user.full_name,
            'phone_number': user.phone_number
        }
    db.close()
    raise ValueError('User not found')


async def delete(username: str) -> bool:
    if user := db.query(User).filter(User.username == username).first():
        db.delete(user)
        if history := db.query(Conversion).filter(Conversion.username == username).all():
            for h in history:
                h.username = 'user_deleted'
        db.commit()
        db.close()
        return True
    db.close()
    return False