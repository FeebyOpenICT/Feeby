from typing import Optional

from sqlalchemy.orm import Session

from Exceptions import UnexpectedInstanceError
from Models import RequestedFeedbackModel
from .RepositoryBase import RepositoryBase


class RequestedFeedbackRepository(RepositoryBase):
    @staticmethod
    def save(requested_feedback: RequestedFeedbackModel, db: Session) -> RequestedFeedbackModel:
        """Save requested feedback instance in database

        Args:
            requested_feedback (RequestedFeedbackModel): requested feedback model
            db (Session): database session

        Raises:
            UnexpectedInstanceError: if requested feedback is not RequestedFeedbackModel instance

        Returns:
            RequestedFeedbackModel: requested feedback as saved in database
        """
        if not isinstance(requested_feedback, RequestedFeedbackModel):
            raise UnexpectedInstanceError

        db.add(requested_feedback)
        db.flush()
        db.refresh(requested_feedback)

        return requested_feedback

    @staticmethod
    def get_by_id(user_id: int, revision_id: int, db: Session) -> Optional[RequestedFeedbackModel]:
        """Get requested feedback by user and revision id

        Args:
            user_id: id of user
            revision_id: id of revision
            db: database session

        Returns:
            Optional RequestedFeedbackModel
        """
        result = db.query(RequestedFeedbackModel).filter(RequestedFeedbackModel.revision_id == revision_id,
                                                         RequestedFeedbackModel.user_id == user_id).first()
        return result
