from typing import List, Optional
from pytest import Session
from Exceptions import DisabledResourceException
from Exceptions.NotFound import NotFound
from Models.UserModel import UserModel
from Repositories.UserRepository import UserRepository
from Schemas.UserSchema import UserPublicSearch


class UserService:
    @staticmethod
    def get_user_by_id(id: int, db: Session) -> UserModel:
        """
        Calls User model to get user by id

        returns user model
        """
        user = UserRepository.get_user_by_id(id=id, db=db)
        return user

    @staticmethod
    def get_user_by_id_or_fail(id: int, db: Session) -> UserModel:
        """Get user by id, if not found raise error

        Args:
            id (int): id of user as saved in database
            db (Session): database session

        Raises:
            NotFound: if user is not found

        Returns:
            UserModel: user
        """
        user = UserService.get_user_by_id(id=id, db=db)

        if not user:
            raise NotFound(resource="user", id=id)

        return user

    @staticmethod
    def get_active_user_by_id(id: int, db: Session) -> UserModel:
        """Get active user by id whilst checking if user exists and is active

        Args:
            id (int): id of user as saved in database
            db (Session): database session

        Returns:
            UserModel: returns active user
        """
        user = UserService.get_user_by_id_or_fail(id=id, db=db)

        if user.disabled == True:
            raise DisabledResourceException(id=id, resource="user")

        return user

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
