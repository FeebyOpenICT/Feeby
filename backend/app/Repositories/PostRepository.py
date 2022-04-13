from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_

from Models import PostModel, UserAccessPostModel, UserModel
from Exceptions import UnexpectedInstanceError


class PostRepository:
    @staticmethod
    def get_posts_from_user_by_id(user_id: int, db: Session) -> List[PostModel]:
        """Get all posts from a user

        Args:
            user_id (int): user id to get all posts from
            db (Session): database session

        Returns:
            List[PostModel]: list of all posts in database made by the user
        """
        result = db.query(PostModel).filter(PostModel.user_id == user_id).all()
        return result

    @staticmethod
    def save(post: PostModel, db: Session) -> PostModel:
        if not isinstance(post, PostModel):
            raise UnexpectedInstanceError

        db.add(post)
        db.commit()

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
    def get_posts_with_access(current_user_id: int, user_id: int, db: Session) -> List[PostModel]:
        """get posts from user that current user has access to

        Args:
            current_user_id (int): id of current user that is requesting the posts from the user that they have access to
            user_id (int): owner of all the posts
            db (Session): database session

        Returns:
            List[PostModel]: list off all posts that current user has access to that belong to user
        """
        result = db.query(PostModel).join(
            UserAccessPostModel, PostModel.id == UserAccessPostModel.post_id
        ).where(
            UserAccessPostModel.user_id == current_user_id,
            PostModel.user_id == user_id
        ).all()
        return result
