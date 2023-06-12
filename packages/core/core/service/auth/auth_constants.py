from enum import Enum


class ErrorCodes(Enum):
    Generic = "AUTH_GENERIC"
    PasswordNotMatch = "PASSWORD_NOT_MATCH"
    PasswordRequirementsNotMetError = "PASSWORD_REQUIREMENTS_NOT_MET"
