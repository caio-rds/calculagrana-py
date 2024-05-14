from app.src.services.database import *
from app.src.schema.conversion import Conversion
from app.src.model.conversion import Conversion as ConversionModel
from sqlalchemy.orm import Session

import uuid
import random

import requests

api_key = 'fca_live_QDqWPms0Hey4Z89DHqhVyzRIuCDVtoUUNzUxCjFj'
base = 'https://api.freecurrencyapi.com/v1'

db: Session = SessionLocal()


def new_id():
    new_uuid = str(uuid.uuid4()).split('-')
    rand = random.randint(1, len(new_uuid) - 1)
    return new_uuid[0] + new_uuid[rand]


async def new_conversion(conversion: ConversionModel) -> ConversionModel:
    conversion.conversion_value = 0

    conversion.conversion_id = new_id()
    conv = Conversion(**conversion.model_dump(exclude_none=True))
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return conversion


async def get_conversion(c_id: str) -> ConversionModel:
    if conv := db.query(Conversion).filter(Conversion.conversion_id == c_id).first():
        return conv
    return None


async def possible_conversions(currencies_param) -> any:
    if currencies_param is None:
        currencies_param = []
    response = requests.get(url=f"{base}/currencies", headers={'apikey': api_key},
                            params={'currencies': currencies_param})
    return response.json()