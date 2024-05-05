from fastapi import FastAPI
from app.src.router import router

app = FastAPI()

app.include_router(router, prefix="/v0")
