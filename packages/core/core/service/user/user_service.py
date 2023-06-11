from core.repository.repo_user import RepoUser


class UserService:
    repo_user: RepoUser

    def __init__(self, repo_user):
        self.repo_user = repo_user

    def get_user_by_id(self, id: str):
        user = self.repo_user.get_user_by_id(id)
        return user
