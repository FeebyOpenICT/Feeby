import pytest
from Models.UserModel import UserModel
from Models.RoleModel import RoleModel
from Repositories.RoleRepository import RoleRepository
from Schemas.RolesEnum import RolesEnum
from sqlalchemy.orm import Session

from Repositories.UserRepository import UserRepository


def test_find_user_by_id(db: Session, current_active_user: UserModel):
    test_user = UserRepository.get_user_by_id(1, db)

    assert isinstance(test_user, UserModel)

    for role in test_user.roles:
        assert isinstance(role, RoleModel)

    assert test_user == current_active_user
    assert isinstance(test_user.id, int)
    assert isinstance(test_user.fullname, str)
    assert isinstance(test_user.canvas_email, str)
    assert isinstance(test_user.canvas_id, int)
    assert isinstance(test_user.disabled, bool)


def test_initiate_user_without_roles():
    with pytest.raises(ValueError):
        user = UserModel("kajshdf", "kajhsdf", 2, False, [])


def test_initiate_user_with_positional_args(db: Session):
    user = UserModel("name", "email", 2, False, [
        RoleRepository.get_role(RolesEnum.ADMIN, db)])
    db.add(user)
    db.commit()

    assert isinstance(user.id, int)
    assert user.canvas_email == "email"
    assert user.fullname == "name"
    assert user.canvas_id == 2
    assert user.disabled == False
    assert user.roles == [RoleRepository.get_role(RolesEnum.ADMIN, db)]


def test_initiate_user_with_missing_values():
    with pytest.raises(TypeError):
        user = UserModel(
            fullname="kjshdf",
            canvas_id=2,
            disabled=False,
            roles=[],
            # canvas_email="1s" # intentionally commented out so it is missing
        )


def test_find_user_by_canvas_id(db: Session, current_active_user: UserModel):
    test_user = UserRepository.get_user_by_canvas_id(
        current_active_user.canvas_id, db)

    assert isinstance(test_user, UserModel)

    for role in test_user.roles:
        assert isinstance(role, RoleModel)

    assert test_user == current_active_user


def test_user_save_self(db: Session):
    test_user = UserModel("test", "ljksd", 999, False, roles=[
        RoleRepository.get_role(RolesEnum.ADMIN, db)])
    db.add(test_user)
    db.commit()

    test_found_user = UserRepository.get_user_by_canvas_id(999, db)

    assert test_found_user == test_user
