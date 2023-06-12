from core.repository.repo_user import RepoUser
from core.service.auth.auth_service import AuthService
from core.service.user.implementation import CreateUserHandler


class UserService:

    def __init__(self, repo_user: RepoUser, auth_service: AuthService):
        self.repo_user = repo_user
        self.auth_service = auth_service
        self.create_user_handler = CreateUserHandler(
            auth_service=auth_service, repo_user=repo_user)

    def get_user_by_id(self, id: str):
        user = self.repo_user.get_user_by_id(id)
        return user

    def create_user(
        self,
        email: str,
        username: str,
        password: str,
        image: str = None,
        bio: str = None
    ):
        user = self.create_user_handler.execute(
            username=username,
            email=email,
            password=password,
            image=image,
            bio=bio
        )
        return user
