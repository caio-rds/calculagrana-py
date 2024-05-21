import datetime
import os
from datetime import timedelta
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET")


async def pwd_hash(pwd: str) -> str:
    return pwd_context.hash(pwd)


async def check_pwd(pwd: str, passwd_hash: str) -> bool:
    return pwd_context.verify(pwd, passwd_hash)


async def encode_token(username: str) -> str:
    payload = {
        "exp": datetime.datetime.now(datetime.UTC) + timedelta(minutes=10),
        "iat": datetime.datetime.now(datetime.UTC),
        "sub": username
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


async def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {'successful': True, 'username': payload.get('sub')}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token expired')
    except jwt.InvalidTokenError:
        return {'successful': False, 'error': 'Invalid token'}
    except jwt.InvalidSignatureError:
        raise HTTPException(status_code=401, detail='Invalid token signature')
    except Exception as e:
        return {'successful': False, 'error': str(e)}


async def auth_wrapper(token: str = Depends(oauth_scheme)) -> dict:
    return await decode_token(token)
