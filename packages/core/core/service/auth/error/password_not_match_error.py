from core.service.auth.auth_constants import ErrorCodes


class PasswordNotMatchError(Exception):
    """
    Error raised when passwords do not match.

    Attributes:
        code (ErrorCodes): The error code representing PasswordNotMatchError.
        message (str): The error message indicating that the passwords do not match.
    """

    def __init__(self):
        self.code = ErrorCodes.PasswordNotMatch
        self.message = "Passwords do not match. Please try again."
