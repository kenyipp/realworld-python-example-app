import re
import bcrypt
from core.service.auth.error.password_not_match_error import PasswordNotMatchError
from core.service.auth.error.password_requirements_not_met_error import PasswordRequirementsNotMetError


class PasswordHandler:

    def encrypt_password(self, password: str) -> str:
        self.validate_password(password)
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    def compare_password(self, password: str, hashed_password: str):
        matched = bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )
        if not matched:
            raise PasswordNotMatchError()

    def validate_password(self, password: str):
        details = []
        if len(password) < 6:
            details.append("The password must be at least 6 characters long")
        password_regex = r'^(?=.*[a-zA-Z])(?=.*\d).+$'
        if not re.search(password_regex, password):
            details.append(
                "The password must contain at least one letter and one digit")
        if details:
            raise PasswordRequirementsNotMetError(details)
