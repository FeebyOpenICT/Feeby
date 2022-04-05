from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_

from Models.PostModel import PostModel
from Models.UserModel import UserModel


class PostRepository:
    """
    Repository class to do with posts
    """
    @staticmethod
    def get_posts_from_user_by_id(user_id: int, db: Session) -> List[PostModel]:
        """
        Gets all the posts from a user by their id

        user_id = integer equal to the the user id

        Returns a list of python Post mapped class from the database
        """
        result = db.query(PostModel).filter(PostModel.user_id == user_id).all()
        return result

    @staticmethod
    def create_post_for_user(title: str, description: str, user: UserModel, db: Session) -> PostModel:
        """
        Create post for a user

        user = UserModel < user you want to create the post for

        Returns the newly created PostModel
        """
        post = PostModel(title=title, description=description, user=user)
        db.add(post)
        db.commit()
        db.refresh(post)
        return post

    @staticmethod
    def get_post_by_id(post_id: int, user_id: int, db: Session) -> Optional[PostModel]:
        result = db.query(PostModel).filter(
            and_(
                PostModel.id == post_id,
                PostModel.user_id == user_id
            )
        ).first()
        return result

    @staticmethod
    def add_users_with_access_to_post(post: PostModel, users: List[UserModel], db: Session) -> PostModel:
        post.users_with_access = list(set(post.users_with_access + users))
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
