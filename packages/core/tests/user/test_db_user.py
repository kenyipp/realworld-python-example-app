import pytest
from core.database.db_factory import DbFactory
from core.utils import dangerous_reset_database
from faker import Faker

faker = Faker()


@pytest.fixture(autouse=True)
def setup():
    dangerous_reset_database()


def test_create_db_user():
    db_factory = DbFactory()

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
