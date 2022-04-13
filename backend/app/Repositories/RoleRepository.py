from sqlalchemy.orm import Session

from Models.RoleModel import RoleModel
from Schemas.RolesEnum import RolesEnum


class RoleRepository:
    @staticmethod
    def get_role(role: RolesEnum, db: Session):
        """
        Gets role object mapping from db
        """
        db_role = db.query(RoleModel).filter(
            RoleModel.title == role).first()
        if not db_role:
            db_role = RoleModel(title=role)
            db.add(db_role)
            db.commit()
        return db_role
