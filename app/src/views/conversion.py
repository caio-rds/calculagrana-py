from typing import Optional

from fastapi import APIRouter, Depends, Request, HTTPException

from app.src.model.conversion import Conversion
from app.src.services.auth import auth_wrapper
from app.src.controller.conversion import new_conversion

router = APIRouter()


@router.post("/")
async def conversion(payload: Conversion, request: Request, username: Optional[dict] = Depends(auth_wrapper)) -> dict:
    if username.get('successful'):
        payload.username = username.get('username')
    payload.request_ip = request.client.host
    if new_conv := await new_conversion(payload):
        return {
            "from_currency": new_conv.from_currency,
            "to_currency": new_conv.to_currency,
            "amount": new_conv.amount,
            "conversion_value": new_conv.conversion_value
        }
    raise HTTPException(status_code=400, detail="Conversion failed")
