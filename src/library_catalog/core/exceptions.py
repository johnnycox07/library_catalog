from uuid import UUID
from typing import Any


class AppException(Exception):
    """Базовое исключение приложения"""

    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={self.message!r}, status_code={self.status_code})"


class NotFoundException(AppException):
    """Исключение: ресурс не найден."""

    def __init__(self, resource: str, identifier: Any):
        super().__init__(
            message=f"{resource} with identifier '{identifier}' not found",
            status_code=404,
        )
        self.resource = resource
        self.identifier = identifier