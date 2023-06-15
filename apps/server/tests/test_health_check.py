import pytest
from server.app import create_app


@pytest.fixture
def client():
    app = create_app()
    yield app.test_client()


def test_health_check(client):
    response = client.get("/api/health-check")
    assert response.status_code == 200
