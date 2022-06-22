from typing import List

from sqlalchemy.orm import Session

from Exceptions import UnexpectedInstanceError
from Models import FeedbackModel, RevisionModel
from .RepositoryBase import RepositoryBase


class FeedbackRepository(RepositoryBase):
    @staticmethod
    def get_by_id(id: int, db: Session) -> FeedbackModel:
        """get feedback by id

        Args:
            id (int): id of feedback
            db (Session): database session

        Returns:
            Optional[FeedbackModel]: Feedback as saved in database
        """
        feedback = db.query(FeedbackModel).filter(
            FeedbackModel.id == id).first()
        return feedback

    @staticmethod
    def save(
            feedback: FeedbackModel,
            db: Session
    ) -> FeedbackModel:
        """Create feedback in db

        Args:
            feedback (FeedbackModel): feedback
            db (Session): database session

        Raises:
            UnexpectedInstance: if instance is not of FeedbackModel

        Returns:
            FeedbackModel: newly created feedback from database
        """
        if not isinstance(feedback, FeedbackModel):
            raise UnexpectedInstanceError

        db.add(feedback)
        db.flush()
        db.refresh(feedback)

        return feedback

    @staticmethod
    def get_all(db: Session) -> List[FeedbackModel]:
        result = db.query(FeedbackModel).all()
        return result

    @staticmethod
    def get_all_from_revision(db: Session, revision_id: int) -> List[FeedbackModel]:
        result = db.query(FeedbackModel).join(RevisionModel, RevisionModel.id == FeedbackModel.revision_id).filter(
            RevisionModel.id == revision_id).all()
        return result

    @staticmethod
    def get_baseline_measurement(post_id: int, db: Session) -> List[FeedbackModel]:
        result = db.execute("""
            SELECT feedback.*
            FROM post 
            JOIN (
            SELECT * from revision
            WHERE id in (
                SELECT min(id) from revision GROUP BY post_id
            )
            ) AS first_revision
            ON post.id = first_revision.post_id
            INNER JOIN feedback
            ON feedback.revision_id = first_revision.id
            WHERE post.id = :post_id
            AND feedback.reviewer_id = post.user_id;
        """, {"post_id": post_id}).fetchall()

        return result
