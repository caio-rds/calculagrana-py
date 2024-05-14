from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.src.model.user import CreateUser, ReadUser
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
            return ReadUser(
                email=user.email,
                username=user.username,
                full_name=user.full_name,
                phone_number=user.phone_number,
                conversions=jsonable_encoder(user_conversions)
            )
        return ReadUser(
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            phone_number=user.phone_number
        )
    return None


async def create(new_user: CreateUser) -> ReadUser:
    new_user.password = await pwd_hash(new_user.password)
    user = User(**new_user.dict())
    if db.query(User).filter(User.email == new_user.email or User.username == new_user.username).first():
        raise HTTPException(status_code=400, detail='User already exists')
    db.add(user)
    db.commit()
    db.refresh(user)
    return ReadUser(
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        phone_number=user.phone_number
    )


async def update(u_id: str, new_data: dict) -> ReadUser:
    pass
    # operation = await update_one('users', {'u_id': u_id}, {'$set': new_data})
    # if operation.modified_count:
    #     return await read(u_id=u_id)
    # raise HTTPException(status_code=500, detail='Failed to update user')


async def delete(u_id: str) -> dict:
    pass
    # operation = await delete_one('users', {'u_id': u_id}, find_and_delete=True)
    # if operation:
    #     return {
    #         'message': 'User deleted',
    #         'user': {
    #             'u_id': operation['u_id'],
    #             'email': operation['email'],
    #             'username': operation['username']
    #         }
    #     }
    # raise HTTPException(status_code=500, detail='Failed to delete user')


async def update_experience(u_id: str, new_data: dict) -> ReadUser:
    pass
    # operation = await update_one('users', {'u_id': u_id}, {'$push': {'professional_experience': new_data}})
    # if operation.modified_count:
    #     return await read(u_id=u_id)
    # raise HTTPException(status_code=500, detail='Failed to update user experience')
