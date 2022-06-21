from typing import List, Optional

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from Exceptions import UnexpectedInstanceError
from Models import PostModel, UserAccessPostModel, RevisionModel, FeedbackModel
from .RepositoryBase import RepositoryBase


class PostRepository(RepositoryBase):
    @staticmethod
    def get_by_id(db: Session, id: int) -> PostModel:
        result = db.query(PostModel).filter(PostModel.id == id).first()
        return result

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
        """Save post instance in database

        Args:
            post (PostModel): post model
            db (Session): database session

        Raises:
            UnexpectedInstanceError: if post is not PostModel instance

        Returns:
            PostModel: post as saved in database
        """
        if not isinstance(post, PostModel):
            raise UnexpectedInstanceError

        db.add(post)
        db.flush()
        db.refresh(post)

        return post

    @staticmethod
    def get_post_by_id_by_user_id(post_id: int, user_id: int, db: Session) -> Optional[PostModel]:
        """get post by id

        Args:
            post_id (int): post id
            user_id (int): id of owner of post
            db (Session): database session

        Returns:
            Optional[PostModel]: post if found or None
        """
        result = db.query(PostModel).filter(
            and_(
                PostModel.id == post_id,
                PostModel.user_id == user_id
            )
        ).first()
        return result

    @staticmethod
    def get_post_with_access(current_user_id: int, post_id: int, db: Session) -> Optional[PostModel]:
        """get post with access

        Args:
            current_user_id (int): current user id
            post_id (int): id of post
            db (Session): database session

        Returns:
            Optional[PostModel]: post or None if no access
        """
        result = db.query(PostModel).join(
            UserAccessPostModel, PostModel.id == UserAccessPostModel.post_id
        ).where(
            or_(and_(
                UserAccessPostModel.user_id == current_user_id,
                UserAccessPostModel.post_id == post_id
            ), and_(PostModel.user_id == current_user_id, PostModel.id == post_id))
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

    @staticmethod
    def get_complete_post_with_access(current_user_id: int, post_id: int, db: Session):
        result = db.query(PostModel).join(UserAccessPostModel, PostModel.id == UserAccessPostModel.post_id,
                                          isouter=True) \
            .join(RevisionModel, PostModel.id == RevisionModel.post_id) \
            .join(FeedbackModel, RevisionModel.id == FeedbackModel.revision_id) \
            .where(
            or_(and_(
                UserAccessPostModel.user_id == current_user_id,
                UserAccessPostModel.post_id == post_id
            ), PostModel.user_id == current_user_id)
        )
        print(result)
        return result
