from typing import List, Optional
from pytest import Session
from Exceptions import DisabledResourceException
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
    def get_active_user_by_id(id: int, db: Session) -> Optional[UserModel]:
        """Get active user by id

        Args:
            id (int): id of user as saved in database
            db (Session): database session

        Returns:
            Optional[UserModel]: returns user or None if user is not found or is disabled
        """
        user = UserRepository.get_user_by_id(id=id, db=db)

        if user.disabled == True:
            raise DisabledResourceException(id=id, resource="user")

        return user

    @staticmethod
    def get_user_by_canvas_id(id: int, db: Session) -> UserModel:
        """
        Calls User model to get user by their canvas_id

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
