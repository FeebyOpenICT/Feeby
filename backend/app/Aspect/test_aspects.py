def test_create_post(client):
    data = {
        "title": "test",
        "short_description": "testshort",
        "description": "testdesc",
        "external_url": "testurl"
    }
    response = client.post("/aspects/", json=data)
    assert response.status_code == 200
    assert response.json()['title'] == "test"
    assert response.json()['short_description'] == "testshort"
    assert response.json()['description'] == "testdesc"
    assert response.json()['external_url'] == "testurl"


def test_empty_get_aspect(client):
    response = client.get("/aspects/")
    assert response.status_code == 200
    assert response.json() == []
