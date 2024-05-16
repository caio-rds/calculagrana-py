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


async def read(username: str, conversions: bool = False) -> ReadUser | None:
    if user := db.query(User).filter(User.username == username).first():
        if conversions:
            user_conversions = db.query(Conversion).filter(Conversion.username == user.username).all()
            db.close()
            return ReadUser(
                email=user.email,
                username=user.username,
                full_name=user.full_name,
                phone_number=user.phone_number,
                conversions=jsonable_encoder(user_conversions)
            )
        db.close()
        return ReadUser(
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            phone_number=user.phone_number
        )
    db.close()
    return None


async def create(new_user: CreateUser) -> ReadUser:
    new_user.password = await pwd_hash(new_user.password)
    user = User(**new_user.dict())
    if db.query(User).filter(User.email == new_user.email or User.username == new_user.username).first():
        db.close()
        raise HTTPException(status_code=400, detail='User already exists')
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return ReadUser(
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        phone_number=user.phone_number
    ).dict(exclude_none=True, exclude={'conversions'})


async def update(user_update: UpdateUser) -> ReadUser:
    if user := db.query(User).filter(User.username == user_update.username).first():
        for key, value in user_update.dict(exclude_unset=True).items():
            if value == getattr(user, key):
                continue
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        db.close()
        return ReadUser(
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            phone_number=user.phone_number
        ).dict(exclude_none=True, exclude={'conversions'})
    db.close()
    raise HTTPException(status_code=404, detail='User not found')


async def delete(username: str) -> dict:
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

