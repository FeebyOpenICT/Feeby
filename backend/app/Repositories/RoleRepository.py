from sqlalchemy.orm import Session

from Models.RoleModel import RoleModel
from Schemas.RolesEnum import RolesEnum


class RoleRepository:
    @staticmethod
    def create_role(role: RolesEnum, db: Session) -> RoleModel:
        role = RoleModel(title=role)

        db.add(role)
        db.commit()

        return role

    @staticmethod
    def get_role(role: RolesEnum, db: Session):
        """
        Gets role object mapping from db
        """
        db_role = db.query(RoleModel).filter(
            RoleModel.title == role).first()
        if not db_role:
            db_role = RoleRepository.create_role(role=role, db=db)
        return db_role
