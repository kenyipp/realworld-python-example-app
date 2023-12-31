from server.error.api_error import APIError
from server.error.default_error_config import error_config

config = error_config["500"]


class APIErrorInternalServerError(APIError):

    def __init__(
        self,
        message=None,
        error_code=None,
        payload=None
    ):
        super().__init__(
            code=500,
            message=message or config["message"],
            error_code=error_code,
            error_type=config["type"],
            payload=payload
        )
