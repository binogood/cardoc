from core.exceptions.base import CustomException


class DecodeTokenException(CustomException):
    code = 400
    error_code = 10000
    message = "Token decode error"


class ExpiredTokenException(CustomException):
    code = 400
    error_code = 10001
    message = "Expired token"


class InvalidTokenException(CustomException):
    code = 400
    error_code = 10002
    message = "Invalid token"


class InvalidTokenSchemeException(CustomException):
    code = 400
    error_code = 10003
    message = "Invalid token scheme"

