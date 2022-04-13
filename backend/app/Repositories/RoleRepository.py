from sqlalchemy.orm import Session

from Models.RoleModel import RoleModel
from Schemas.RolesEnum import RolesEnum


class RoleRepository:
    @staticmethod
    def create_role(role: RolesEnum, db: Session) -> RoleModel:
        """Create role in database

        Args:
            role (RolesEnum): One of the roles as described in RolesEnum
            db (Session): database session

        Returns:
            RoleModel: newly created role as saved in database
        """
        role = RoleModel(title=role)

        db.add(role)
        db.commit()

        return role

    @staticmethod
    def get_role(role: RolesEnum, db: Session) -> RoleModel:
        """Get role from database by role title from RolesEnum or create new one if it does not exist yet

        Args:
            role (RolesEnum): One of the roles as described in RolesEnum
            db (Session): database session

        Returns:
            RoleModel: role as saved in database
        """
        db_role = db.query(RoleModel).filter(
            RoleModel.title == role).first()
        if not db_role:
            db_role = RoleRepository.create_role(role=role, db=db)
        return db_role
