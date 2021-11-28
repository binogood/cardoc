from cardoc.core.exceptions.base import CustomException


class DuplicateCarTrimException(CustomException):
    code = 400
    error_code = 30000
    message = "Duplicate car trim"


class CarNotFoundException(CustomException):
    code = 404
    error_code = 30001
    message = "Car not found"


class DuplicateCarTireException(CustomException):
    code = 400
    error_code = 30002
    message = "Duplicate car tire"
