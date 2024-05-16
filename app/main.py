from fastapi import FastAPI
import logging

from app.src.router import router

app = FastAPI(
    version="0.1",
    title="Currency Converter",
    description="A simple currency converter API"
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

app.include_router(router, prefix="/v0")


