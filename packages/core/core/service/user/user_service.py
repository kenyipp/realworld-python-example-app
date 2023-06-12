from core.repository.repo_user import RepoUser
from core.service.auth.auth_service import AuthService


class UserService:

    def __init__(self, repo_user: RepoUser, auth_service: AuthService):
        self.repo_user = repo_user
        self.auth_service = auth_service

    def get_user_by_id(self, id: str):
        user = self.repo_user.get_user_by_id(id)
        return user
