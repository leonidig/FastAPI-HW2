from fastapi import HTTPException


class UserAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "User already exists!"):
        super().__init__(status_code=400, detail=detail)


class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = "User not found!"):
        super().__init__(status_code=404, detail=detail)