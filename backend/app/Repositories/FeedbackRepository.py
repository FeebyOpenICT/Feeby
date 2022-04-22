from typing import List
from sqlalchemy.orm import Session
from Exceptions import UnexpectedInstanceError
from .RepositoryBase import RepositoryBase
from Models import FeedbackModel


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
        db.commit()

        return feedback

    @staticmethod
    def get_all(db: Session) -> List[FeedbackModel]:
        result = db.query(FeedbackModel).all()
        return result
