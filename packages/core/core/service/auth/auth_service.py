from core.service.auth.implementation.password_handler import PasswordHandler


class AuthService:

    def __init__(self):
        self.password_handler = PasswordHandler()

    def encrypt_password(self, password: str):
        encrypted = self.password_handler.encrypt_password(password=password)
        return encrypted

    def compare_password(self, password: str, encryptedPassword: str):
        matched = self.password_handler.compare_password(
            password, encryptedPassword)
        return matched
