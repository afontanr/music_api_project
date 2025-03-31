from rest_framework import status

class APIException(Exception):
    def __init__(
        self,
        detail: str = "Server Error",
        code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        log: str = None
    ):
        self.detail = detail
        self.code = code
        self.log = log

class NotFoundException(APIException):
    def __init__(self, resource: str):
        super().__init__(
            detail=f"{resource} not found",
            code=status.HTTP_404_NOT_FOUND
        )