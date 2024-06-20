from fastapi import APIRouter, HTTPException, Request

from app.src.controller.recovery import user_request_code, recovery_by_password, recovery_by_code
from app.src.controller.user import create, read, update, delete
from app.src.model.user import (CreateUser, ReadUser, RequestUpdateUser, UpdatedUser, ResponseRecovery, RecoveryByCode,
                                RecoveryByPassword, Recovered)

router = APIRouter()


@router.post('/', response_model=ReadUser, response_model_exclude_unset=True)
async def create_user(new_user: CreateUser) -> ReadUser:
    return await create(new_user)


@router.get('/{identifier}', response_model=ReadUser, response_model_exclude_unset=True)
async def get_user(identifier: str, conversions: bool = False, find_by: str = 'id') -> ReadUser:
    params_values = ['id', 'username', 'email']
    if find_by not in params_values:
        raise HTTPException(
            status_code=400,
            detail='Invalid parameter find_by, must be id (default), username or email'
        )
    return await read(identifier, conversions, find_by)


#
@router.put('/', response_model=UpdatedUser, response_model_exclude_unset=True)
async def update_user(user: RequestUpdateUser) -> UpdatedUser:
    return await update(user)


@router.delete('/{username}')
async def delete_user(username: str):
    return await delete(username)


@router.post('/request_code/{username}', response_model=ResponseRecovery)
async def request_code(username: str, request: Request) -> ResponseRecovery:
    return await user_request_code(username, request.client.host)


@router.post('/recovery/code', response_model=Recovered)
async def reset_password(recovery: RecoveryByCode) -> Recovered:
    if recovered := await recovery_by_code(recovery):
        return Recovered(success=recovered, message='Password updated successfully')


@router.post('/recovery/password', response_model=Recovered)
async def reset_password(recovery: RecoveryByPassword) -> Recovered:
    if recovered := await recovery_by_password(recovery):
        return Recovered(success=recovered, message='Password updated successfully')
