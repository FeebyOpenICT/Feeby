from typing import List, Optional

from sqlalchemy import and_
from sqlalchemy.orm import Session, aliased

from Exceptions import UnexpectedInstanceError
from Models import PostModel, AspectModel, RatingModel, UserModel
from Models.FeedbackModel import FeedbackModel
from Models.RevisionModel import RevisionModel
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
        result = db.query(PostModel).filter(PostModel.user_id == user_id).order_by(PostModel.time_created.desc()).all()
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
    def get_complete_post_with_access(post_id: int, db: Session):
        reviewer_alias = aliased(UserModel)
        result = db.query(PostModel) \
            .join(RevisionModel, RevisionModel.post_id == PostModel.id) \
            .join(FeedbackModel, FeedbackModel.revision_id == RevisionModel.id) \
            .join(AspectModel, FeedbackModel.aspect_id == AspectModel.id) \
            .join(RatingModel, FeedbackModel.rating_id == RatingModel.id) \
            .join(UserModel, PostModel.user_id == UserModel.id) \
            .join(reviewer_alias, FeedbackModel.reviewer_id == reviewer_alias.id) \
            .filter(PostModel.id == post_id) \
            .first()
        return result
