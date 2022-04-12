from Models.PostModel import PostModel
from sqlalchemy.orm import Session

from Models.UserModel import UserModel
from Repositories.RoleRepository import RoleRepository
from Schemas.RolesEnum import RolesEnum


def test_post_create_post(client):
    data = {
        "title": "test",
        "description": "testdesc"
    }
    response = client.post("/users/1/posts", json=data)
    assert response.status_code == 201
    assert response.json()['title'] == "test"
    assert response.json()['description'] == "testdesc"


def test_get_empty_posts(client):
    response = client.get("/users/1/posts")
    assert response.status_code == 200
    assert response.json() == []


def test_get_posts_self(client, db, current_active_user):
    post1, post2 = PostModel("title1", "desc1", current_active_user), PostModel(
        "title2", "desc2", current_active_user)
    post1.save_self(db)
    post2.save_self(db)

    print("ignore me")

    response = client.get('/users/1/posts')

    assert response.status_code == 200
    assert len(response.json()) == 2

    assert response.json()[0]['title'] == post1.title
    assert response.json()[0]['title'] == post1.title

    assert response.json()[1]['title'] == post2.title
    assert response.json()[1]['description'] == post2.description


def test_get_posts_from_user_that_doesnt_exist(client, db: Session):
    response = client.get('/users/2/posts')

    json = response.json()
    assert response.status_code == 404
    assert json['detail'] == 'Requested user: 2 not found in database'
    assert json['id'] == 2
    assert json['resource'] == 'user'