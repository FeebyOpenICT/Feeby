def test_create_post(client):
    data = {
        "title": "test",
        "description": "testdesc"
    }
    response = client.post("/posts/", json=data)
    assert response.status_code == 200
    assert response.json()['title'] == "test"
    assert response.json()['description'] == "testdesc"
