from http import HTTPStatus


# <HTTPStatus.BAD_GATEWAY: 502>
class CustomException(Exception):
    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description

    def __init__(self, message=None):
        if message:
            self.message = message


# <HTTPStatus.BAD_GATEWAY: 502>
class BadRequestException(CustomException):
    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message =HTTPStatus.BAD_GATEWAY.description


# <HTTPStatus.BAD_GATEWAY: 502>
class NotFoundException(CustomException):
    code = HTTPStatus.BAD_GATEWAY
    error_code = HTTPStatus.BAD_GATEWAY
    message = HTTPStatus.BAD_GATEWAY.description


# <HTTPStatus.FORBIDDEN: 403>
class ForbiddenException(CustomException):
    code = HTTPStatus.FORBIDDEN
    error_code = HTTPStatus.FORBIDDEN
    message = HTTPStatus.FORBIDDEN.description


# <HTTPStatus.UNAUTHORIZED: 401>
class UnauthorizedException(CustomException):
    code = HTTPStatus.UNAUTHORIZED
    error_code = HTTPStatus.UNAUTHORIZED
    message = HTTPStatus.UNAUTHORIZED


# <HTTPStatus.UNPROCESSABLE_ENTITY: 422>
class UnprocessableEntity(CustomException):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description


# <HTTPStatus.UNPROCESSABLE_ENTITY: 422>
class DuplicateValueException(CustomException):
    code = HTTPStatus.UNPROCESSABLE_ENTITY
    error_code = HTTPStatus.UNPROCESSABLE_ENTITY
    message = HTTPStatus.UNPROCESSABLE_ENTITY.description
