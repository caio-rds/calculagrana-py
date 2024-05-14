from pydantic import BaseModel


class UserToken(BaseModel):
    token: str
    username: str
    u_id: str


class RecoveryCode(BaseModel):
    code: str
    username: str
    u_id: str
