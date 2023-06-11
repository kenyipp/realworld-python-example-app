import pytest
from core.database.db_factory import DbFactory
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import clear_database, connection_string, migrate_database

faker = Faker()


@pytest.fixture
def hydrate_database():
    migrate_database()
    yield
    clear_database()


def test_create_user(hydrate_database):
    engine = create_engine(connection_string, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    db_factory = DbFactory(session=session)

    db_user = db_factory.new_db_user()

    user_id = db_user.create_user(
        faker.user_name(),
        faker.email(),
        faker.paragraph(),
        None,
        faker.password()
    )

    user = db_user.get_user_by_id(user_id)

    assert user is not None

    engine.dispose()
