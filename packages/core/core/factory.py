from core.repository.repo_factory import RepoFactory
from core.service.auth.auth_service import AuthService
from core.service.user.user_service import UserService


class Factory:
    def __init__(self, session) -> None:
        self.repo_factory = RepoFactory(session)

    def new_auth_service(self):
        auth_service = AuthService()
        return auth_service

    def new_user_service(self):
        repo_user = self.repo_factory.new_repo_user()
        auth_service = self.new_auth_service()
        user_service = UserService(
            repo_user=repo_user,
            auth_service=auth_service
        )
        return user_service
