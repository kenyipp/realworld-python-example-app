import pytest
from core.factory import Factory
from core.service.auth.error import (PasswordNotMatchError,
                                     PasswordRequirementsNotMetError)
from faker import Faker

faker = Faker()


def test_encrypt_password_password_length_less_than_6():
    factory = Factory()
    auth_service = factory.new_auth_service()

    with pytest.raises(expected_exception=PasswordRequirementsNotMetError) as error:
        auth_service.encrypt_password(password="abc12")

    assert isinstance(error.value, PasswordRequirementsNotMetError)
    assert len(error.value.details) == 1


def test_password_requirements_not_met_error():
    factory = Factory()
    auth_service = factory.new_auth_service()

    with pytest.raises(PasswordRequirementsNotMetError) as error:
        auth_service.encrypt_password(password="abcdef")

    assert isinstance(error.value, PasswordRequirementsNotMetError)
    assert len(error.value.details) == 1


def test_encrypt_password():
    factory = Factory()
    auth_service = factory.new_auth_service()

    hashed = auth_service.encrypt_password(password="123abc")
    assert hashed is not None


def test_encrypt_and_verify_password():
    factory = Factory()
    auth_service = factory.new_auth_service()

    password = "123abc"
    hashed = auth_service.encrypt_password(password=password)
    assert hashed is not None

    auth_service.compare_password(password=password, encryptedPassword=hashed)


def test_password_not_match_error():
    factory = Factory()
    auth_service = factory.new_auth_service()

    password = "123abc"
    hashed = auth_service.encrypt_password(password=password)
    assert hashed is not None
    assert isinstance(hashed, str)

    with pytest.raises(PasswordNotMatchError):
        auth_service.compare_password(
            password="abc123", encryptedPassword=hashed)
