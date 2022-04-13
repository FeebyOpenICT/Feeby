from typing import List, Optional
from pytest import Session
from Models.UserModel import UserModel
from Repositories.UserRepository import UserRepository
from Schemas.UserSchema import UserPublicSearch


class UserService:
    @staticmethod
    def get_user_by_id(id: int, db: Session) -> Optional[UserModel]:
        """Get user by id

        Args:
            id (int): id of user
            db (Session): database session

        Returns:
            Optional[UserModel]: user or None
        """
        user = UserRepository.get_user_by_id(id=id, db=db)
        return user

    @staticmethod
    def get_user_by_canvas_id(id: int, db: Session) -> Optional[UserModel]:
        """Get user by their canvas id

        Args:
            id (int): canvas id of user
            db (Session): database session

        Returns:
            Optional[UserModel]: user or None
        """
        return UserRepository.get_user_by_canvas_id(id=id, db=db)

    @staticmethod
    def get_user_ids_by_name_or_email(query: str, db: Session) -> List[UserPublicSearch]:
        """Get users by searching through their names and emails

        Args:
            query (str): string to search through name and emails with
            db (Session): database session

        Returns:
            List[UserPublicSearch]: list of public data from users
        """
        public_list_of_users = UserRepository.get_user_ids_by_name_or_email(
            query=query, db=db)
        return public_list_of_users
