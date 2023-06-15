from typing import List

from core.service.auth.auth_constants import ErrorCodes


class PasswordRequirementsNotMetError(Exception):
    """
    Error raised when password requirements are not met.

    Attributes:
        code (ErrorCodes): The error code representing PasswordNotMatchError.
        message (str): The error message indicating that password requirements are not met.
        details (List[str]): Additional details about the password requirements not being met.
    """

    def __init__(self, details: List[str]):
        self.code = ErrorCodes.PasswordRequirementsNotMetError
        self.message = "Password requirements not met. \
            Your password must be at least 6 characters long and contain at least one letter and one digit.",
        self.details = details
