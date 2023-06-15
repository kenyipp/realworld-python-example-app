import pytest
from core.constants import RecordStatus
from core.factory import Factory
from core.service.user.error import UserExistError
from core.utils import dangerous_reset_database
from faker import Faker

faker = Faker()


@pytest.fixture(autouse=True)
def setup():
    dangerous_reset_database()


def test_create_user():
    factory = Factory()
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


def test_create_user_username_taken_error():
    factory = Factory()
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


def test_create_user_email_used_error():
    factory = Factory()
    user_service = factory.new_user_service()
    factory = Factory()
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
