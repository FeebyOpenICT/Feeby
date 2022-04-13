from typing import List, Optional
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from Exceptions.NotFound import NotFound
from Models.UserModel import UserModel
from Schemas.UserSchema import UserPublicSearch


class UserRepository:
    @staticmethod
    def get_user_by_canvas_id(id: int, db: Session) -> Optional[UserModel]:
        """Get user by their canvas id

        Args:
            id (int): canvas id as saved in database
            db (Session): database session

        Returns:
            Optional[UserModel]: user from database or None
        """
        user = db.query(UserModel).filter(UserModel.canvas_id == id).first()
        return user

    @staticmethod
    def get_user_by_id(id: int, db: Session) -> Optional[UserModel]:
        """Get user by their id

        Args:
            id (int): id as saved in database
            db (Session): database session

        Returns:
            Optional[UserModel]: user from database or None
        """
        user = db.query(UserModel).filter(UserModel.id == id).first()
        return user

    @staticmethod
    def get_user_ids_by_name_or_email(query: str, db: Session) -> List[UserPublicSearch]:
        """Search through users saved in database and return first 10 hits

        Args:
            query (str): string that will search through email and fullname columns
            db (Session): database session

        Returns:
            List[UserPublicSearch]: list of details that are open to the public
        """
        users = db.query(UserModel).with_entities(
            UserModel.canvas_email,
            UserModel.id,
            UserModel.fullname
        ).filter(
            or_(
                and_(UserModel.canvas_email.ilike(
                    f"%{query}%"), UserModel.disabled == False),
                and_(UserModel.fullname.ilike(
                    f"%{query}%"), UserModel.disabled == False)
            )
        ).limit(
            10
        ).all()

        return users
