from fastapi import APIRouter, HTTPException, Request

from app.src.controller.user import create, read, update
# from app.src.controller.recovery import user_request_code, recovery_by_password, recovery_by_code
from app.src.model.user import CreateUser, ReadUser, RequestUpdateUser, UpdatedUser
from app.src.services.email import new_email

router = APIRouter()


@router.post('/', response_model=ReadUser, response_model_exclude_unset=True)
async def create_user(new_user: CreateUser) -> ReadUser:
    try:
        return await create(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
    pass

# @router.post('/request_code/{username}', response_model=ResponseRecovery)
# async def request_code(username: str, request: Request) -> ResponseRecovery:
#     pass
# try:
#     if req_code := await user_request_code(username, request.client.host):
#         await new_email(req_code['send_to'], req_code['code'])
#         return ResponseRecovery(
#             username=req_code['username'],
#             send_to=req_code['send_to'],
#             request_ip=req_code['request_ip'],
#             code=req_code['code'],
#             request_date=req_code['request_date']
#         )
# except Exception as e:
#     code = 500
#     if str(e) == 'User not found':
#         code = 404
#     raise HTTPException(status_code=code, detail=str(e))


# @router.post('/recovery/code')
# async def reset_password(recovery: RecoveryByCode):
#     pass
# try:
#     if await recovery_by_code(recovery):
#         return {
#             'status': 'success',
#             'message': 'Password updated successfully'
#         }
#     raise HTTPException(status_code=404, detail='User not found')
# except ValueError as e:
#     raise HTTPException(status_code=400, detail=str(e))
# except Exception as e:
#     raise HTTPException(status_code=500, detail=str(e))


# @router.post('/recovery/password')
# async def reset_password(recovery: RecoveryByPassword):
#     pass
# try:
#     if await recovery_by_password(recovery):
#         return {
#             'status': 'success',
#             'message': 'Password updated successfully'
#         }
#     raise HTTPException(status_code=404, detail='User not found')
# except ValueError as e:
#     raise HTTPException(status_code=400, detail=str(e))
# except Exception as e:
#     raise HTTPException(status_code=500, detail=str(e))
