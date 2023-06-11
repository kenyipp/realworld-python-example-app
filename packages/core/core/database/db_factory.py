from core.database.db_user import DbUser
from sqlalchemy.orm import Session


class DbFactory:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def new_db_user(self):
        db_user = DbUser(self.session)
        return db_user
