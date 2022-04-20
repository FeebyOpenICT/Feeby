from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_

from Models import PostModel, UserAccessPostModel, UserModel


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
    def get_post_with_access(current_user_id: int, post_id: int, db: Session) -> Optional[PostModel]:
        result = db.query(PostModel).join(
            UserAccessPostModel, PostModel.id == UserAccessPostModel.post_id
        ).where(
            and_(
                UserAccessPostModel.user_id == current_user_id,
                UserAccessPostModel.post_id == post_id
            )
        ).first()
        return result

    @staticmethod
    def get_posts_with_access(current_user_id: int, user_id: int, db: Session) -> Optional[PostModel]:
        result = db.query(PostModel).join(
            UserAccessPostModel, PostModel.id == UserAccessPostModel.post_id
        ).where(
            UserAccessPostModel.user_id == current_user_id,
            PostModel.user_id == user_id
        ).all()
        return result
