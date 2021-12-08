from core.exceptions.base import CustomException


class DuplicateTireException(CustomException):
    code = 400
    error_code = 20000
    message = "duplicate tire"


class TireNotFoundException(CustomException):
    code = 404
    error_code = 20001
    message = "tire not found"


class DuplicateTireTypeException(CustomException):
    code = 400
    error_code = 20002
    message = "duplicate tire type"


class TireTypeNotFoundException(CustomException):
    code = 404
    error_code = 20003
    message = "tire type not found"
