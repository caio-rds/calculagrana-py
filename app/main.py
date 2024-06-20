import os
import threading

from beanie import init_beanie
from fastapi import FastAPI
import logging

from app.src.model.conversion import Currency, Conversion
from app.src.model.logs import Log
from app.src.model.user import CreateUser, ReadUser, UpdatedUser, Login, TryLogin, Recovery
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
                CreateUser, ReadUser, Currency, Conversion, UpdatedUser, Login, TryLogin, Recovery, Log
            ]
        )
        logging.info('Beanie initialized with MongoDB')
        # threading.Thread(target=await update_all_currencies()).start()
        logging.info('Currencies update thread started')
    except Exception as e:
        logging.error(f'Error initializing Beanie with MongoDB: {e}')


app.include_router(router, prefix="/v1")


