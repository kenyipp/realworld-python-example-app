from core.service import UserService
from core.service.auth.error import PasswordRequirementsNotMetError
from core.service.user.error import UserExistError
from server.error import APIErrorBadRequest, APIErrorConflict
from server.user.dto import DtoUser


class APIRegistration():
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def execute(
        self,
        username: str,
        email: str,
        password: str,
        image: str
    ):
        try:
            db_dto_user = self.user_service.create_user(
                username=username,
                email=email,
                password=password,
                image=image
            )
            dto_user = DtoUser(db_dto_user=db_dto_user)
            return {
                "user": dto_user
            }
        except PasswordRequirementsNotMetError:
            raise APIErrorBadRequest(
                message="Password requirements not met. \
                    Your password must be at least 6 characters long and contain at least one letter and one digit."
            )
        except UserExistError:
            raise APIErrorConflict(
                message="The provided email or username is already registered. \
                    Please use a different email or username."
            )
        except Exception as error:
            raise error
