class AppException(Exception):
    def __init__(self, message: str, error_type: str):
        self.message = message
        self.error_type = error_type


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, "not_found")


class ConflictException(AppException):
    def __init__(self, message: str = "Resource conflict"):
        super().__init__(message, "conflict")


class BadRequestException(AppException):
    def __init__(self, message: str = "Bad request"):
        super().__init__(message, "bad_request")
