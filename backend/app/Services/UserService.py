from typing import List, Optional
from pytest import Session
from Exceptions import DisabledResourceException
from Exceptions.NotFoundException import NotFoundException
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
        user = UserRepository.get_user_by_id(id=id, db=db)

        if not user:
            raise NotFoundException(resource="user", id=id)

        return user

    @staticmethod
    def get_active_user_by_id_or_fail(id: int, db: Session) -> UserModel:
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
    def get_user_by_canvas_id(id: int, db: Session) -> Optional[UserModel]:
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
        return UserRepository.get_user_ids_by_name_or_email(query=query, db=db)

    @staticmethod
    def get_user_by_canvas_id_or_fail(id: int, db: Session) -> UserModel:
        """Get user by canvas id or throw not found if no user

        Args:
            id (int): user id
            db (Session): database session

        Raises:
            NotFound: if user is not found

        Returns:
            UserModel: user
        """
        user = UserRepository.get_user_by_canvas_id(id=id, db=db)

        if not user:
            raise NotFoundException(resource="user", id=id)

        return user
