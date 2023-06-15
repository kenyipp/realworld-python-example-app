from sqlalchemy import MetaData, create_engine
from utils import dangerous_reset_database, connection_string


def test_database_migration():
    dangerous_reset_database()
    engine = create_engine(connection_string, echo=False)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    tables = metadata.tables
    assert len(tables) > 2
    engine.dispose()
