import os
import threading

from beanie import init_beanie
from fastapi import FastAPI
import logging

from app.src.models.conversion import Currency, Conversion
from app.src.models.logs import Log
from app.src.models.user import CreateUser, ReadUser, UpdatedUser, TryUpdateUsername
from app.src.models.login import Login, TryLogin
from app.src.models.recovery import Recovery
from motor.motor_asyncio import AsyncIOMotorClient
from app.src.router import router
from app.src.services.free_currency import update_all_currencies

app = FastAPI(version="0.2", title="Currency Converter", description="A simple currency converter API")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


@app.on_event("startup")
async def app_init():
    try:
        client = AsyncIOMotorClient(os.getenv('MONGO_URL'))
        await init_beanie(
            database=client.get_database('currency_py'),
            document_models=[
                CreateUser, ReadUser, Currency, Conversion, UpdatedUser, Login, TryLogin, Recovery, Log,
                TryUpdateUsername
            ]
        )
        logging.info('Beanie initialized with MongoDB')
        threading.Thread(target=await update_all_currencies()).start()
    except Exception as e:
        logging.error(f'Error initializing Beanie with MongoDB: {e}')


app.include_router(router, prefix="/v1")


