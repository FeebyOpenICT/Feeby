import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    test_string = 'ak;jlshdflkhjasdf'
    response = client.get(f"/{test_string}")
    assert response.status_code == 200
    assert response.json() == {
        "message": f"{test_string}this has been updated"
    }

if __name__ == "__main__":
    pytest()
