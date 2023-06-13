from core.repository.repo_user import RepoUser
from core.service.auth.auth_service import AuthService
from core.service.user.error import UserExistError


class CreateUserHandler:

    def __init__(self, auth_service: AuthService, repo_user: RepoUser):
        self.auth_service = auth_service
        self.repo_user = repo_user

    def execute(
        self,
        email: str,
        username: str,
        password: str,
        image: str = None,
        bio: str = None
    ):
        is_existed = self.repo_user.is_user_exist(username, email)
        if is_existed:
            raise UserExistError()
        encrypted = self.auth_service.encrypt_password(password=password)
        user_id = self.repo_user.create_user(
            username=username,
            email=email,
            bio=bio,
            image=image,
            password_hash=encrypted
        )
        user = self.repo_user.get_user_by_id(user_id)
        return user
