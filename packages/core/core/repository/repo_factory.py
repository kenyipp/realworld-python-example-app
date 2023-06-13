from core.database.db_factory import DbFactory
from core.repository.repo_user import RepoUser


class RepoFactory:

    def __init__(self):
        self.db_factory = DbFactory()

    def new_repo_user(self):
        db_user = self.db_factory.new_db_user()
        return RepoUser(db_user)
