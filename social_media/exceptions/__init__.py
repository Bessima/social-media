from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND


class AppException(Exception):
    status: int

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}: Occurred error: {self.status}"


class NotFoundException(AppException):
    status: int = HTTP_404_NOT_FOUND
    message: str


class BadRequestException(AppException):
    status: int = HTTP_400_BAD_REQUEST
    message: str
