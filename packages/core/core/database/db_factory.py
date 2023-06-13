from core.database.db_user import DbUser


class DbFactory:

    def new_db_user(self):
        db_user = DbUser()
        return db_user
