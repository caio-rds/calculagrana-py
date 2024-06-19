# from typing import Optional
#
from typing import Optional

from fastapi import APIRouter, Depends, Request, HTTPException

from app.src.model.conversion import Conversion, ConversionRequest
from app.src.controller.conversion import possible_conversions, new_conversion, get_conversion_by_id
from app.src.utils.auth import auth_wrapper

router = APIRouter()


@router.post("/", response_model_exclude_unset=True, response_model=Conversion)
async def conversion(payload: ConversionRequest,
                     request: Request,
                     username: Optional[dict] = Depends(auth_wrapper)) -> Conversion:
    if username.get('successful'):
        payload.username = username.get('username')
    payload.user_agent = request.headers.get('User-Agent')
    payload.request_ip = request.client.host
    if new_conv := await new_conversion(payload):
        return new_conv
    raise HTTPException(status_code=400, detail="Conversion failed")


@router.get("/search/{conversion_id}", response_model=Conversion)
async def get_conversion(conversion_id: str) -> Conversion:
    if conv := await get_conversion_by_id(conversion_id=conversion_id):
        return conv


@router.get("/currencies")
async def get_currencies(currencies: str = None) -> list:
    return await possible_conversions(currencies)
