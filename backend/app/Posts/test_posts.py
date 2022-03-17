def test_create_post(client):
    data = {
        "title": "test",
        "description": "testdesc"
    }
    response = client.post("/posts/", json=data)
    assert response.status_code == 200
    assert response.json()['title'] == "test"
    assert response.json()['description'] == "testdesc"


def test_empty_get_post(client):
    response = client.get("/posts/self")
    assert response.status_code == 200
    assert response.json() == []
