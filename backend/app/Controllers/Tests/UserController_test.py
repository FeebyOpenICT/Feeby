
from Models.UserModel import UserModel
from Schemas.RolesEnum import RolesEnum
from Repositories.RoleRepository import RoleRepository
from sqlalchemy.orm import Session

from Services import RoleService


def test_get_user_self(client, current_active_user):
    response = client.get("/users/self")

    assert response.status_code == 200
    assert response.json()['id'] == current_active_user.id
    assert response.json()['fullname'] == current_active_user.fullname
    assert response.json()['canvas_email'] == current_active_user.canvas_email
    assert response.json()['canvas_id'] == current_active_user.canvas_id
    assert response.json()['disabled'] == current_active_user.disabled

    for res_role, query_role in zip(response.json()['roles'], current_active_user.roles):
        assert res_role['title'] == query_role.title
        assert res_role['id'] == query_role.id


def test_get_user_by_id(client, current_active_user):
    response = client.get("/users/self")

    assert response.status_code == 200
    assert response.json()['id'] == current_active_user.id
    assert response.json()['fullname'] == current_active_user.fullname
    assert response.json()['canvas_email'] == current_active_user.canvas_email
    assert response.json()['canvas_id'] == current_active_user.canvas_id
    assert response.json()['disabled'] == current_active_user.disabled

    for res_role, query_role in zip(response.json()['roles'], current_active_user.roles):
        assert res_role['title'] == query_role.title
        assert res_role['id'] == query_role.id


def test_get_user_by_id_not_found(client):
    response = client.get('/users/999999/canvas')

    json = response.json()
    assert response.status_code == 404
    assert json['detail'] == "Requested user: 999999 not found in database"
    assert json['resource'] == "user"
    assert json['id'] == 999999


def test_get_user_by_canvas_id(client, db: Session):
    # setup new user
    new_user_json = {
        "fullname": "testmename",
        "canvas_id": 2,
        "canvas_email": "testmeemail@hu.nl",
        "disabled": False,
        "roles": [
            RoleService.get_or_create_role(RolesEnum.ADMIN, db),
            RoleService.get_or_create_role(RolesEnum.CONTENT_DEVELOPER, db),
            RoleService.get_or_create_role(RolesEnum.INSTRUCTOR, db),
        ]
    }

    new_user = UserModel(**new_user_json)
    db.add(new_user)
    db.commit()

    response = client.get(f"/users/{new_user_json['canvas_id']}/canvas")

    assert response.status_code == 200
    assert response.json()['id'] == new_user.id
    assert response.json()['fullname'] == new_user.fullname
    assert response.json()['canvas_email'] == new_user.canvas_email
    assert response.json()['canvas_id'] == new_user.canvas_id
    assert response.json()['disabled'] == new_user.disabled

    for res_role, query_role in zip(response.json()['roles'], new_user.roles):
        assert res_role['title'] == query_role.title
        assert res_role['id'] == query_role.id


def test_get_user_by_canvas_id_not_found(client):
    response = client.get('/users/999999/canvas')

    json = response.json()
    assert response.status_code == 404
    assert json['detail'] == "Requested user: 999999 not found in database"
    assert json['resource'] == "user"
    assert json['id'] == 999999
