import pytest
from core.factory import Factory
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import clear_database, connection_string, migrate_database
from core.constants import RecordStatus
from core.service.user.error import UserExistError

faker = Faker()


@pytest.fixture(autouse=True)
def hydrate_database():
    migrate_database()
    yield
    clear_database()


def test_create_user():
    engine = create_engine(connection_string, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    factory = Factory(session=session)
    user_service = factory.new_user_service()

    user_body = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password()
    }

    user = user_service.create_user(**user_body)
    assert user is not None
    assert user.username == user_body["username"]
    assert user.email == user_body["email"]
    assert user.record_status == RecordStatus.Normal
    assert user.bio is None
    assert user.image is None

    engine.dispose()


def test_create_user_username_taken_error():
    engine = create_engine(connection_string, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    factory = Factory(session=session)
    user_service = factory.new_user_service()

    user_body = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password()
    }

    user_service.create_user(**user_body)
    with pytest.raises(UserExistError):
        user_service.create_user(
            username=user_body["username"],
            email=faker.email(),
            password=user_body["password"]
        )

    engine.dispose()


def test_create_user_email_used_error():
    engine = create_engine(connection_string, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    factory = Factory(session=session)
    user_service = factory.new_user_service()

    user_body = {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.password()
    }

    user_service.create_user(**user_body)
    with pytest.raises(UserExistError):
        user_service.create_user(
            username=faker.user_name(),
            email=user_body["email"],
            password=user_body["password"]
        )

    engine.dispose()
