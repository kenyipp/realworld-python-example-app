import pytest
from sqlalchemy import MetaData, create_engine
from utils import clear_database, connection_string, migrate_database


def test_database_migration():
    migrate_database()
    engine = create_engine(connection_string, echo=False)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tables = metadata.tables
    assert len(tables) > 2
    engine.dispose()
    clear_database()
