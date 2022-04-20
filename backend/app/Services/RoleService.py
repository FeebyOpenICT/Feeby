from Models.RoleModel import RoleModel
from Schemas import RolesEnum
from sqlalchemy.orm import Session
from Repositories import RoleRepository


class RoleService:
    @staticmethod
    def get_or_create_role(role: RolesEnum, db: Session) -> RoleModel:
        """Get or create role from or in db

        Args:
            role (RolesEnum): title of role as defined in enum
            db (Session): database session

        Returns:
            RoleModel: role as saved in database
        """
        role_in_db = RoleRepository.get_role_by_title(role=role, db=db)

        if not role_in_db:
            role_in_db = RoleRepository.save(role=RoleModel(title=role), db=db)

        return role_in_db
