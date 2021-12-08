from core.exceptions.base import CustomException


class DecodeTokenException(CustomException):
    code = 400
    error_code = 10000
    message = "Token decode error"


class ExpiredTokenException(CustomException):
    code = 400
    error_code = 10001
    message = "Expired token"