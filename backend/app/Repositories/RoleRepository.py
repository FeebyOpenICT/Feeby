from typing import Optional
from sqlalchemy.orm import Session
from Exceptions import UnexpectedInstanceError

from Models.RoleModel import RoleModel
from Schemas.RolesEnum import RolesEnum


class RoleRepository:
    @staticmethod
    def save(role: RoleModel, db: Session) -> RoleModel:
        """save role in database

        Args:
            role (RoleModel): role
            db (Session): database session

        Raises:
            UnexpectedInstance: if instance is not of RoleModel

        Returns:
            RoleModel: newly created role as saved in database
        """
        if not isinstance(role, RoleModel):
            raise UnexpectedInstanceError

        db.add(role)

        return role

    @staticmethod
    def get_role_by_title(role: RolesEnum, db: Session) -> Optional[RoleModel]:
        """Get role from database by role title from RolesEnum or create new one if it does not exist yet

        Args:
            role (RolesEnum): One of the roles as described in RolesEnum
            db (Session): database session

        Returns:
            Optional[RoleModel]: role as saved in database
        """
        db_role = db.query(RoleModel).filter(
            RoleModel.title == role).first()

        return db_role
