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


def test_initiate_user_without_roles(db: Session):
    with pytest.raises(ValueError):
        user = User("kajshdf", "kajhsdf", 2, False, [])


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
