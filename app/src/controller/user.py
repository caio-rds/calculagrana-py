from beanie.operators import Set
from bson import ObjectId
from app.src.models.conversion import Conversion
from app.src.models.user import ReadUser, CreateUser, RequestUpdateUser, UpdatedUser, UserDeleted, \
    RequestUpdateUsername, ResponseUpdateUsername, TryUpdateUsername
from app.src.models.login import Login
from app.src.utils.auth import pwd_hash
from app.src.utils.custom_exceptions import UserNotFound, GenericException
from app.src.utils.validations import validate_bson
from pymongo.errors import DuplicateKeyError


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
        raise UserNotFound

    if user := await ReadUser.aggregate([
        {'$match': queries.get(find_by, None)},
        {'$lookup': {'from': 'conversions', 'localField': 'username', 'foreignField': 'username', 'as': 'conversions'}}
    ]).to_list():
        return user[0]
    raise UserNotFound


async def create(new_user: CreateUser) -> ReadUser:
    try:
        new_user.password = await pwd_hash(new_user.password)
        user = await new_user.insert()
        return ReadUser(**user.model_dump())
    except DuplicateKeyError:
        raise GenericException(message='User already exists', status_code=400)


async def update(user_update: RequestUpdateUser) -> UpdatedUser:
    if user := await UpdatedUser.find_one(UpdatedUser.username == user_update.username):
        for key, value in user_update.dict(exclude_unset=True).items():
            if key == 'password':
                value = await pwd_hash(value)
            setattr(user, key, value)
        await user.save()
        return user
    raise UserNotFound


async def update_username(request_user: RequestUpdateUsername) -> ResponseUpdateUsername:
    if user := await UpdatedUser.find_one(UpdatedUser.username == request_user.username):
        if await ReadUser.find_one(ReadUser.username == request_user.new_username):
            raise GenericException(message=f'New username {request_user.new_username} already in use', status_code=400)
        user.username = request_user.new_username
        await user.save()
        await (Conversion.find(Conversion.username == request_user.username).
               update({'$set': {'username': request_user.new_username}}))
        return ResponseUpdateUsername(
            username=user.username,
            new_username=request_user.new_username,
            message='Username updated successfully',
            status=True
        )
    raise UserNotFound


async def delete(username: str):
    if user := await ReadUser.find_one(ReadUser.username == username):
        await user.delete()
        if user_has_conversions := await Conversion.find_one(Conversion.username == username):
            await user_has_conversions.delete()
        if login_history := await Login.find_one(Login.username == username):
            await login_history.delete()
        return UserDeleted(
            username=user.username,
            message='User deleted successfully',
            status=True,
            id=str(user.id)
        )
    raise UserNotFound
