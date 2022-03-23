import pytest
from Models.User import User
from Models.Role import Role, Roles
from sqlalchemy.orm import Session


def test_find_user_by_id(db: Session, current_active_user: User):
    test_user = User.get_user_by_id(1, db)

    assert isinstance(test_user, User)

    for role in test_user.roles:
        assert isinstance(role, Role)

    assert test_user == current_active_user
    assert isinstance(test_user.id, int)
    assert isinstance(test_user.fullname, str)
    assert isinstance(test_user.canvas_email, str)
    assert isinstance(test_user.canvas_id, int)
    assert isinstance(test_user.disabled, bool)


def test_initiate_user_without_roles():
    with pytest.raises(ValueError):
        user = User("kajshdf", "kajhsdf", 2, False, [])


def test_initiate_user_with_positional_args(db: Session):
    user = User("name", "email", 2, False, [Role.get_role(Roles.ADMIN, db)])
    user.save_self(db)

    assert isinstance(user.id, int)
    assert user.canvas_email == "email"
    assert user.fullname == "name"
    assert user.canvas_id == 2
    assert user.disabled == False
    assert user.roles == [Role.get_role(Roles.ADMIN, db)]


def test_initiate_user_with_missing_values():
    with pytest.raises(TypeError):
        user = User(
            fullname="kjshdf",
            canvas_id=2,
            disabled=False,
            roles=[],
            # canvas_email="1s" # intentionally commented out so it is missing
        )


def test_find_user_by_canvas_id(db: Session, current_active_user: User):
    test_user = User.get_user_by_canvas_id(current_active_user.canvas_id, db)

    assert isinstance(test_user, User)

    for role in test_user.roles:
        assert isinstance(role, Role)

    assert test_user == current_active_user


def test_user_save_self(db: Session):
    test_user = User("test", "ljksd", 999, False, roles=[
                     Role.get_role(Roles.ADMIN, db)])
    test_user.save_self(db)

    test_found_user = User.get_user_by_canvas_id(999, db)

    assert test_found_user == test_user
