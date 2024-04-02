from typing import TypeVar, Generic

T = TypeVar('T')

class Response(Generic[T]):
    message: str = ""
    status_code: int
    data : T
    success: bool = True,
    exceptions: list

    def __init__(self, message, status_code, data, success, exception):
        self.message = message
        self.status_code = status_code
        self.data = data
        self.success = success
        self.exceptions = exception