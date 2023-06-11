import pytest
from sqlalchemy import MetaData, create_engine
from utils import clear_database, connection_string, migrate_database


@pytest.fixture
def hydrate_database():
    migrate_database()
    yield
    clear_database()


def test_database_migration(hydrate_database):
    engine = create_engine(connection_string, echo=False)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tables = metadata.tables
    assert len(tables) > 2
    engine.dispose()
