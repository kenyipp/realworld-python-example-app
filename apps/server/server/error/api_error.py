class APIError(Exception):
    def __init__(
        self,
        code: int,
        message: str,
        error_code: str,
        error_type=None,
        payload=None
    ):
        self.code = code
        self.message = message
        self.error_code = error_code
        self.error_type = error_type
        self.payload = payload
