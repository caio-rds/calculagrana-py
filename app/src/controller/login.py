import datetime

from app.src.services.auth import encode_token, check_pwd
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.src.schema.user import User
from app.src.services.database import SessionLocal

db: Session = SessionLocal()


async def upsert_token(username: str) -> str:
    if user := db.query(User).filter(User.username == username).first():
        user.token = await encode_token(user.username)
        user.login_at = datetime.datetime.now(datetime.UTC)
        db.commit()
        db.refresh(user)
        db.close()
        return user.token

    raise HTTPException(status_code=404, detail='User not found')


async def match_user(username: str, password: str) -> bool:
    if user := db.query(User).filter(User.username == username).first():
        return await check_pwd(password, user.password)
    return False
