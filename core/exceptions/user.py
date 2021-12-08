from core.exceptions.base import CustomException


class DuplicateNameException(CustomException):
    code = 400
    error_code = 20000
    message = "duplicate email"


class UserNotFoundException(CustomException):
    code = 404
    error_code = 20001
    message = "User not found"


class DuplicateUserCarException(CustomException):
    code = 400
    error_code = 20002
    message = "duplicate User Car"


class ManyRequestsException(CustomException):
    code = 400
    error_code = 20003
    message = "Many requests"