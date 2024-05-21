import datetime
import logging
import threading
import time
import os
import requests
from fastapi import HTTPException

from app.src.services.database import SessionLocal
from app.src.schema.conversion import Conversion, Currencies
from app.src.model.conversion import Conversion as ConversionModel
from sqlalchemy.orm import Session

import uuid
import random

db: Session = SessionLocal()

all_currencies = {}

api_key = os.getenv('FREECURRENCY_KEY')
base = 'https://api.freecurrencyapi.com/v1'


def new_id():
    new_uuid = str(uuid.uuid4()).split('-')
    rand = random.randint(1, len(new_uuid) - 1)
    return new_uuid[0] + new_uuid[rand]


async def new_conversion(conversion: ConversionModel) -> ConversionModel:
    conversion.conversions = await convert(conversion.amount, conversion.base_currency, conversion.to_currency)
    conversion.conversion_id = new_id()
    conv = Conversion(**conversion.model_dump(exclude_none=True, exclude={'to_currency'}))
    db.add(conv)
    db.commit()
    db.close()
    logging.log(level=logging.INFO, msg=f"New conversion created: {conversion.conversion_id} by {conversion.username}")
    return conversion


async def get_conversion(c_id: str) -> ConversionModel:
    if conv := db.query(Conversion).filter(Conversion.conversion_id == c_id).first():
        logging.log(level=logging.INFO, msg=f"Conversion found: {c_id}")
        conv_model = ConversionModel(
            base_currency=conv.base_currency,
            to_currency=[key for key in conv.conversions.keys()],
            amount=conv.amount,
            conversions=conv.conversions,
            username=conv.username,
            request_ip=conv.request_ip,
            conversion_id=conv.conversion_id
        )
        return conv_model
    logging.log(level=logging.INFO, msg=f"Conversion not found: {c_id}")
    return None


async def possible_conversions(currencies) -> any:
    result = {}
    if currencies is None or currencies == []:
        consult = db.query(Currencies).all()
    else:
        consult = db.query(Currencies).filter(Currencies.code.in_(currencies.split(','))).all()

    for c in consult:
        result.update({
            c.code: {
                'name': c.name,
                'name_plural': c.name_plural,
                'code': c.code
            }
        })

    return result


async def convert(amount: float, base_currency: str, to_currency: str or list) -> any:
    result = {}
    if all_currencies:
        if isinstance(to_currency, str):
            to_currency = [to_currency]
        for currency in to_currency:
            if all_currencies.get(currency):
                currency_value = all_currencies.get(currency).get('value')
                base_currency_value = all_currencies.get(base_currency).get('value')
                result.update({
                    currency: {
                        'amount': round((amount / base_currency_value) * currency_value, 2),
                        'unit_value': round((currency_value / all_currencies.get(base_currency).get('value')), 2)
                    }
                })
        return result
    raise HTTPException(status_code=500, detail="Try again later.")


def update_all_currencies():
    while True:
        currencies = requests.get(url=f"{base}/currencies", headers={'apikey': api_key}).json().get('data')
        currencies_values = requests.get(url=f"{base}/latest", headers={'apikey': api_key},
                                         params={'base_currency': 'EUR'}).json().get('data')
        if currency_exists := db.query(Currencies).filter(Currencies.code.in_(currencies.keys())).all():
            for currency in currency_exists:
                currency.c_value = currencies_values.get(currency.code)
                currency.updated_at = datetime.datetime.now(datetime.UTC)
        else:
            for key, value in currencies.items():
                conv = Currencies(
                    code=key,
                    name=value.get('name'),
                    name_plural=value.get('name_plural'),
                    c_value=currencies_values.get(key),
                    base_currency='EUR',
                    updated_at=datetime.datetime.now(datetime.UTC)
                )
                db.add(conv)
        db.commit()
        db.close()
        logging.log(level=logging.INFO, msg="Updating currencies in Database, next in 6000 seconds.")
        for key, value in currencies.items():
            all_currencies.update({
                key: {
                    'name': value.get('name'),
                    'name_plural': value.get('name_plural'),
                    'code': key,
                    'value': currencies_values.get(key),
                    'base_currency': 'EUR',
                    'updated_at': datetime.datetime.now(datetime.UTC)
                }
            })
        logging.log(level=logging.INFO, msg="Currencies Server updated.")
        time.sleep(6000)


threading.Thread(target=update_all_currencies).start()
