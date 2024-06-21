import datetime
import logging
import os
import time

import requests as r

from app.src.models.conversion import Currency

api_key = os.getenv('FREE_CURRENCY_KEY')
base = 'https://api.freecurrencyapi.com/v1'


class FreeCurrency:

    @staticmethod
    def all_currencies():
        result = {}
        response = r.get(f'{base}/currencies', headers={'apikey': api_key}).json().get('data')
        for key, value in response.items():
            result.update({
                key: {
                    'name': value.get('name'),
                    'name_plural': value.get('name_plural'),
                    'code': key
                }
            })
        return result

    @staticmethod
    def latest_rates(base_currency: str = 'EUR'):
        response = (r.get(f'{base}/latest', headers={'apikey': api_key}, params={'base_currency': base_currency}).
                    json())
        return response.get('data')


async def update_all_currencies():
    logging.info('Currencies update thread started')
    while True:
        currencies = FreeCurrency.all_currencies()
        latest = FreeCurrency.latest_rates()
        for key, value in latest.items():
            currencies[key].update({'value': round(value, 2), 'base_currency': 'EUR'})

        for key, value in currencies.items():
            if currency := await Currency.find_one(Currency.code == key):
                currency.value = value.get('value')
                currency.updated_at = datetime.datetime.now()
                await currency.save()
                continue
            await Currency(**value).save()

        time.sleep(6000)
