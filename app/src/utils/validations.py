from bson import BSON, ObjectId
from bson.errors import InvalidId

from app.src.utils.custom_exceptions import InvalidID


async def to_bson(identifier: str) -> ObjectId:
    if isinstance(identifier, str):
        try:
            return ObjectId(identifier)
        except InvalidId:
            raise InvalidID(message=f'Invalid ID {identifier}')


async def validate_bson(identifier: str) -> bool:
    if not ObjectId.is_valid(identifier):
        raise InvalidID(message='Invalid ID')
    return True
