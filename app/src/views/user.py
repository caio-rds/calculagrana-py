from fastapi import APIRouter, HTTPException, Request

from app.src.controller.recovery import user_request_code, recovery_by_password, recovery_by_code
from app.src.model.user import CreateUser, UpdateUser, ReadUser, ResponseRecovery, RecoveryByCode, RecoveryByPassword
from app.src.controller.user import create, read, update, delete
from app.src.services.email import new_email

router = APIRouter()


@router.post('/', response_model=ReadUser, response_model_exclude_unset=True)
async def create_user(new_user: CreateUser) -> ReadUser:
    try:
        creation = await create(new_user)
        return ReadUser(**creation)
    except ValueError:
        raise HTTPException(status_code=409, detail='User already exists')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/{username}', response_model=ReadUser, response_model_exclude_unset=True)
async def get_user(username: str, conversions: bool = False) -> ReadUser:
    try:
        if user := await read(username, conversions):
            return ReadUser(**user)
        raise HTTPException(status_code=404, detail='User not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put('/', response_model=ReadUser, response_model_exclude_unset=True)
async def update_user(user: UpdateUser) -> ReadUser:
    try:
        if updated := await update(user):
            return ReadUser(**updated)
    except ValueError:
        raise HTTPException(status_code=404, detail=str('User not found'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/{username}')
async def delete_user(username: str):
    try:
        if await delete(username):
            return {
                'status': 'success',
                'message': f'User {username} deleted successfully'
            }
        raise HTTPException(status_code=404, detail='User not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/request_code/{username}', response_model=ResponseRecovery)
async def request_code(username: str, request: Request) -> ResponseRecovery:
    try:
        if req_code := await user_request_code(username, request.client.host):
            await new_email(req_code['send_to'], req_code['code'])
            return ResponseRecovery(
                username=req_code['username'],
                send_to=req_code['send_to'],
                request_ip=req_code['request_ip'],
                code=req_code['code'],
                request_date=req_code['request_date']
            )
    except Exception as e:
        code = 500
        if str(e) == 'User not found':
            code = 404
        raise HTTPException(status_code=code, detail=str(e))


@router.post('/recovery/code')
async def reset_password(recovery: RecoveryByCode):
    try:
        if await recovery_by_code(recovery):
            return {
                'status': 'success',
                'message': 'Password updated successfully'
            }
        raise HTTPException(status_code=404, detail='User not found')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/recovery/password')
async def reset_password(recovery: RecoveryByPassword):
    try:
        if await recovery_by_password(recovery):
            return {
                'status': 'success',
                'message': 'Password updated successfully'
            }
        raise HTTPException(status_code=404, detail='User not found')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
