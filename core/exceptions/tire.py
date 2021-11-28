from cardoc.core.exceptions.base import CustomException


class DuplicateTireException(CustomException):
    code = 400
    error_code = 20000
    message = "duplicate front tire"


class TireNotFoundException(CustomException):
    code = 404
    error_code = 20001
    message = "tire not found"


class DuplicateTireTypeException(CustomException):
    code = 400
    error_code = 20000
    message = "duplicate rear tire"


class TireTypeNotFoundException(CustomException):
    code = 404
    error_code = 20001
    message = "tire type not found"
