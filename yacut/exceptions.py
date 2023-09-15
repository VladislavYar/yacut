from http import HTTPStatus
from typing import Union


class InvalidAPIUsage(Exception):
    """Класс исключений API."""
    status_code = HTTPStatus.NOT_FOUND

    def __init__(self, message: str,
                 status_code: Union[int, None] = None) -> None:
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self) -> dict:
        """Преобразует сообщение в словарь."""
        return {'message': self.message}