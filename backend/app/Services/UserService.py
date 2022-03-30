from typing import List
from pytest import Session
from Models.User import UserModel
from Repositories.UserRepository import UserRepository
from Schemas.UserSchema import UserPublicSearch


class UserService:
    @staticmethod
    def get_user_by_id(id: int, db: Session) -> UserModel:
        """
        Calls User model to get user by id

        returns user model
        """
        return UserRepository.get_user_by_id(id=id, db=db)

    @staticmethod
    def get_user_by_canvas_id(id: int, db: Session) -> UserModel:
        """
        Calls User model to get user by their canvas_id

        returns user model
        """
        return UserRepository.get_user_by_canvas_id(id=id, db=db)

    @staticmethod
    def get_user_ids_by_name_or_email(query: str, db: Session) -> List[UserPublicSearch]:
        """
        Calls UserRepository to get public user data by name or email

        returns list of users with their id, fullname and canvas_email
        """
        return UserRepository.get_user_ids_by_name_or_email(query=query, db=db)
