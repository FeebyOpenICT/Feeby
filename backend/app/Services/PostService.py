from typing import List
from sqlalchemy.orm import Session
from Exceptions.NotFound import NotFound

from Models.PostModel import PostModel
from Models.UserModel import UserModel
from Repositories.PostRepository import PostRepository
from Repositories.UserRepository import UserRepository


class PostService:
    @staticmethod
    def get_posts_from_user_by_id(user_id: int, db: Session) -> List[PostModel]:
        """
        Gets all the posts from a user by their id

        user_id = integer equal to the the user id

        Returns a list of python Post mapped class from the database
        """
        result = PostRepository.get_posts_from_user_by_id(
            user_id=user_id, db=db)
        return result

    @staticmethod
    def create_post_for_user_by_id(title: str, description: str, user_id: int, db: Session) -> PostModel:
        user = UserRepository.get_user_by_id(id=user_id, db=db)

        if user is None:
            raise NotFound(resource="user", id=user_id)

        post = PostRepository.create_post_for_user(
            title=title, description=description, user=user, db=db)

        return post

    @staticmethod
    def create_post_for_user_by_model(title: str, description: str, user: UserModel, db: Session) -> PostModel:
        post = PostRepository.create_post_for_user(
            title=title, description=description, user=user, db=db)

        return post
