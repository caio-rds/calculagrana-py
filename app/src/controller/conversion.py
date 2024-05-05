from app.src.services.database import *
from app.src.schema.conversion import Conversion
from app.src.model.conversion import Conversion as ConversionModel
from sqlalchemy.orm import Session
from currency_converter import CurrencyConverter
import uuid
import random

converter = CurrencyConverter()

db: Session = SessionLocal()


def new_id():
    new_uuid = str(uuid.uuid4()).split('-')
    rand = random.randint(1, len(new_uuid) - 1)
    return new_uuid[0] + new_uuid[rand]


async def new_conversion(conversion: ConversionModel) -> ConversionModel:
    conversion.conversion_value = round(
        converter.convert(conversion.amount, conversion.from_currency, conversion.to_currency), 2)
    conversion.conversion_id = new_id()
    conv = Conversion(**conversion.model_dump(exclude_none=True))
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return conversion
