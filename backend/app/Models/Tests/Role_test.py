from Models.RoleModel import RoleModel
from Repositories.RoleRepository import RoleRepository
from Schemas.RolesEnum import RolesEnum
from sqlalchemy.orm import Session

from Services import RoleService


def test_get_role(db: Session):
    test_role = RoleService.get_or_create_role(RolesEnum.ADMIN, db)

    assert isinstance(test_role, RoleModel)
    assert test_role.title == RolesEnum.ADMIN
    assert isinstance(test_role.id, int)
