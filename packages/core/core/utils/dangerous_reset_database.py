from os import path

from alembic import command
from alembic.config import Config

db_file = "db.sqlite3"
migration_path = path.join(path.dirname(__file__), "../../migration")
connection_string = "sqlite:///{}".format(db_file)


def dangerous_reset_database():
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", migration_path)
    alembic_cfg.set_main_option("sqlalchemy.url", connection_string)
    command.downgrade(alembic_cfg, "base")
    command.upgrade(alembic_cfg, "head")
