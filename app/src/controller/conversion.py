import logging
from difflib import SequenceMatcher

from app.src.model.conversion import Currency, ConversionRequest, Conversion, ResultConversion
from app.src.utils.custom_exceptions import NotFound
from beanie.operators import In

from app.src.utils.logs import create_log
from app.src.utils.validations import to_bson


async def new_conversion(conversion: ConversionRequest) -> Conversion:
    new_conv = Conversion(**conversion.model_dump())
    new_conv.conversions = await convert(conversion.amount, conversion.base_currency, conversion.to_currency)
    await new_conv.save()
    logging.log(level=logging.INFO, msg=f"New conversion created: {new_conv.id} by {new_conv.username}")
    await create_log(
        title="New conversion",
        action=f"New conversion {new_conv.id} created",
        user_trigger=new_conv.username,
        level="INFO"
    )
    return new_conv


async def get_conversion_by_id(conversion_id: str) -> Conversion:
    if b_id := await to_bson(conversion_id):
        if conversion := Conversion.get(b_id):
            return await conversion
    raise NotFound("Conversion not found")


async def possible_conversions(currencies: str) -> list[Currency]:
    if currencies is None:
        if all_currencies := Currency.find_all(projection_model=Currency):
            return await all_currencies.to_list(length=100)
    if currencies_consult := Currency.find(In(Currency.code, currencies.split(','))):
        return await currencies_consult.to_list(length=100)
    raise NotFound("Currency not found")


async def convert(amount: float, base_currency: str, to_currency: str or list) -> any:
    result = []
    if isinstance(to_currency, str):
        to_currency = [to_currency]
    if all_currencies := Currency.find_all(projection_model=Currency):
        for currency in await all_currencies.to_list(length=100):
            if currency.code == base_currency:
                base_currency = currency
                break
        for currency in await all_currencies.to_list(length=100):
            if currency.code in to_currency:
                result.append(ResultConversion(
                    code=currency.code,
                    value=round(amount * currency.value / base_currency.value, 2),
                    last_update=currency.updated_at
                ))

        return result
    raise NotFound("Currency not found")


async def did_you_mean(currency: str) -> any:
    higher = 0
    suggestion = None
    for key in await Currency.find_all().to_list():
        match = SequenceMatcher(None, currency, key.code).ratio()
        if match > 0.5 and match > higher:
            higher = match
            suggestion = key
            continue
        return suggestion
