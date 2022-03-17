def test_users_get_self(client):
    response = client.get("/users/self")
    assert response.status_code == 200
