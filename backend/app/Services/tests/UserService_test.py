from typing import List
from Models import UserModel
from sqlalchemy.orm import Session
from Repositories import RoleRepository, UserRepository
from Schemas import UserPublicInDB, RolesEnum
from Services import RoleService


def test_get_user_by_id(current_active_user: UserModel, db: Session) -> UserModel:
    user = UserRepository.get_user_by_id(id=current_active_user.id, db=db)
    assert user == current_active_user


def test_get_non_existing_user_by_id(db: Session) -> UserModel:
    user = UserRepository.get_user_by_id(id=999, db=db)
    assert user == None


def test_get_user_by_canvas_id(current_active_user: UserModel, db: Session) -> UserModel:
    user = UserRepository.get_user_by_canvas_id(
        id=current_active_user.canvas_id, db=db)
    assert user == current_active_user


def test_get_user_ids_by_name_or_email(db: Session) -> List[UserPublicInDB]:
    user1 = UserModel("alex not duncan", "alex.not.duncan", 22, False, [
                      RoleService.get_or_create_role(RolesEnum.STUDENT, db)])
    user2 = UserModel("tim", "tim.duncan", 323, False, [
                      RoleService.get_or_create_role(RolesEnum.STUDENT, db)])

    db.add_all([user1, user2])
    db.commit()

    users = UserRepository.get_user_ids_by_name_or_email(query="alex", db=db)

    assert len(users) == 2
