from Models.RoleModel import RoleModel
from Repositories.RoleRepository import RoleRepository
from Schemas.RolesSchema import RolesEnum
from sqlalchemy.orm import Session


def test_get_role(db: Session):
    test_role = RoleRepository.get_role(RolesEnum.ADMIN, db)

    assert isinstance(test_role, RoleModel)
    assert test_role.title == RolesEnum.ADMIN
    assert isinstance(test_role.id, int)
