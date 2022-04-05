from Models.Role import Roles, RoleModel
from sqlalchemy.orm import Session


def test_get_role(db: Session):
    test_role = RoleModel.get_role(Roles.ADMIN, db)

    assert isinstance(test_role, RoleModel)
    assert test_role.description == Roles.ADMIN['description']
    assert test_role.title == Roles.ADMIN['title']
    assert isinstance(test_role.id, int)
