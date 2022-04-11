from typing import List
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from Exceptions.NotFound import NotFound
from Models.UserModel import UserModel
from Schemas.UserSchema import UserPublicSearch


class UserRepository:
    @staticmethod
    def get_user_by_canvas_id(id: int, db: Session) -> UserModel:
        """
        Gets the user by their canvas id

        id = integer equal to the the canvas id

        Returns a python user mapped class from the database
        """
        user = db.query(UserModel).filter(UserModel.canvas_id == id).first()
        return user

    @staticmethod
    def get_user_by_id(id: int, db: Session) -> UserModel:
        """
        Gets the user by their id

        id = integer equal to the the id

        Returns a python user mapped class from the database
        """
        user = db.query(UserModel).filter(UserModel.id == id).first()
        return user

    @staticmethod
    def get_user_ids_by_name_or_email(query: str, db: Session) -> List[UserPublicSearch]:
        """
        Gets first 10 users by their name or email

        only returns canvas_email, id and fullname
        empty list if none
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
