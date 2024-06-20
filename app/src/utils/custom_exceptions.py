from fastapi import HTTPException


class NotFound(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        raise HTTPException(status_code=404, detail=self.message)


class GenericException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
        raise HTTPException(status_code=self.status_code, detail=self.message)


class InvalidID(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        raise HTTPException(status_code=400, detail=self.message)


class PasswordMismatch(GenericException):
    def __init__(self):
        super().__init__('Password does not match', 400)


class UserNotFound(GenericException):
    def __init__(self):
        super().__init__('User not found', 404)


class CodeNotFound(GenericException):
    def __init__(self):
        super().__init__('Code not found', 404)
