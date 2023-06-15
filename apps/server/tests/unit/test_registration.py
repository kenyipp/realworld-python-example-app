from uuid import uuid4

import pytest
from core.utils import dangerous_reset_database
from faker import Faker
from server.app import create_app

faker = Faker()


@pytest.fixture
def client():
    dangerous_reset_database()
    app = create_app()
    yield app.test_client()


def test_register_user_account(client):
    user_data = {
        "user": {
            "username": faker.user_name(),
            "email": faker.email(),
            "password": str(uuid4())
        }
    }
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 200
    user = response.json["user"]
    assert user is not None
    assert user["email"] is not None
    assert user["username"] is not None
    assert "bio" in user
    assert "image" in user
    assert user["token"] is not None


def test_missing_required_fields(client):
    user_data = {
        "user": {
            "username": faker.user_name()
        }
    }
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 422


def test_duplicate_username_or_email(client):
    user_data = {
        "user": {
            "username": "Jacob",
            "email": "jake@jake.jake",
            "password": "jake123"
        }
    }
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 200
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 409


def test_invalid_password_policy(client):
    user_data = {
        "user": {
            "username": "Jacob",
            "email": "jake@jake.jake",
            "password": "abcdef"
        }
    }
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 400
