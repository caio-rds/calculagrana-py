from bson import ObjectId

from app.src.model.user import ReadUser, CreateUser, RequestUpdateUser, UpdatedUser
from app.src.utils.auth import pwd_hash
from app.src.utils.custom_exceptions import NotFound
from app.src.utils.validations import validate_bson


async def read(identifier: str, conversions: bool = False, find_by: str = 'id') -> ReadUser:
    queries = {
        'username': ReadUser.username == identifier,
        'email': ReadUser.email == identifier.replace('%40', '@')
    }
    if find_by == 'id':
        if await validate_bson(identifier):
            queries['id'] = ReadUser.id == ObjectId(identifier)
    if not conversions:
        if user := await ReadUser.find_one(queries.get(find_by, None)):
            return user
        raise NotFound('User not found')

    if user := await ReadUser.aggregate([
        {'$match': queries.get(find_by, None)},
        {'$lookup': {'from': 'conversions', 'localField': 'username', 'foreignField': 'username', 'as': 'conversions'}}
    ]).to_list():
        return user[0]
    raise NotFound('User not found')


async def create(new_user: CreateUser) -> ReadUser:
    try:
        new_user.password = await pwd_hash(new_user.password)
        user = await new_user.save()
        return ReadUser(**user.model_dump())
    except Exception as e:
        print(e)


async def update(user_update: RequestUpdateUser) -> UpdatedUser:
    if user := await UpdatedUser.find_one(UpdatedUser.username == user_update.username):
        for key, value in user_update.dict(exclude_unset=True).items():
            if key == 'password':
                value = await pwd_hash(value)
            setattr(user, key, value)
        await user.save()
        return user
    raise NotFound('User not found')






#
#
# async def delete(username: str) -> bool:
#     if user := db.query(User).filter(User.username == username).first():
#         db.delete(user)
#         if history := db.query(Conversion).filter(Conversion.username == username).all():
#             for h in history:
#                 h.username = 'user_deleted'
#         db.commit()
#         db.close()
#         return True
#     db.close()
#     return False
