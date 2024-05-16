from typing import Optional

from fastapi import APIRouter, Depends, Request, HTTPException

from app.src.model.conversion import Conversion
from app.src.services.auth import auth_wrapper
from app.src.controller.conversion import new_conversion, get_conversion as get_conv, possible_conversions

router = APIRouter()


@router.post("/")
async def conversion(payload: Conversion, request: Request, username: Optional[dict] = Depends(auth_wrapper)) -> dict:
    if username.get('successful'):
        payload.username = username.get('username')
    payload.request_ip = request.client.host
    if new_conv := await new_conversion(payload):
        return {
            "base_currency": new_conv.base_currency,
            "to_currency": new_conv.to_currency,
            "amount": new_conv.amount,
            "conversions": new_conv.conversions
        }
    raise HTTPException(status_code=400, detail="Conversion failed")


@router.get("/search/{c_id}", response_model=Conversion)
async def get_conversion(c_id: str) -> Conversion:
    if conv := await get_conv(c_id):
        return conv
    raise HTTPException(status_code=400, detail="Conversion not found")


@router.get("/currencies")
async def get_currencies(currencies: str = None) -> dict:
    return await possible_conversions(currencies)