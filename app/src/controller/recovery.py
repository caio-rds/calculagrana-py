import datetime
import random

from app.src.controller.user import read
from app.src.utils.auth import pwd_hash, check_pwd
from app.src.models.login import TryLogin
from app.src.models.recovery import Recovery, RecoveryByCode, RecoveryByPassword, ResponseRecovery
from app.src.utils.custom_exceptions import PasswordMismatch, UserNotFound, CodeNotFound


async def user_request_code(username: str, ip: str) -> ResponseRecovery:
    if user := await read(identifier=username, conversions=False, find_by='username'):
        if code := await Recovery.find_one(Recovery.username == username and Recovery.used == 0):
            return ResponseRecovery(**code.model_dump())
        code = Recovery(
            username=username,
            code=await generate_code(),
            send_to=user.email
        )
        await code.save()
        return ResponseRecovery(**code.model_dump())


async def generate_code() -> str:
    while True:
        code = ''
        for i in range(6):
            code += str(random.randint(0, 9))
        if not await Recovery.find_one(Recovery.code == code):
            return code


async def recovery_by_code(recovery: RecoveryByCode) -> bool:
    if code := await Recovery.find_one(
            Recovery.username == recovery.username and
            Recovery.code == recovery.code and
            Recovery.used == 0
    ):
        if user := await TryLogin.find_one(TryLogin.username == recovery.username):
            user.password = await pwd_hash(recovery.new_password)
            await user.save()
            code.used = 1
            code.used_date = datetime.datetime.now(datetime.timezone.utc)
            await code.save()
            return True
        raise UserNotFound
    raise CodeNotFound


async def recovery_by_password(recovery: RecoveryByPassword) -> bool:
    if user := await TryLogin.find_one(TryLogin.username == recovery.username):
        if await check_pwd(recovery.password, user.password):
            user.password = await pwd_hash(recovery.new_password)
            await user.save()
            return True
        raise PasswordMismatch
    raise UserNotFound
