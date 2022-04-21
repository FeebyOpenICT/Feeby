from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, null
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from Models.AspectModel import AspectModel
from Models.PostModel import PostModel
from Models.RatingModel import RatingModel
from Models.UserModel import UserModel
from database import Base


class FeedbackModel(Base):
    """FeedbackModel
    """
    __tablename__ = 'feedback'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    description: str = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship('PostModel')

    reviewed_feedback_id = Column(
        Integer, ForeignKey('feedback.id'), nullable=True)
    reviewed_feedback = relationship('FeedbackModel')

    aspect_id = Column(Integer, ForeignKey('aspect.id'), nullable=False)
    aspect = relationship('AspectModel')

    rating_id = Column(Integer, ForeignKey('rating.id'), nullable=False)
    rating = relationship('RatingModel')

    reviewer_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    reviewer = relationship('UserModel')

    def __init__(self, description: str, aspect: AspectModel, rating: RatingModel, reviewer: UserModel, post: PostModel, reviewed_feedback=None) -> None:
        """FeedbackModel contstructor

        Args:
            description (str): Description of the feedback
            aspect (AspectModel): Aspect that the feedback has been given on
            rating (RatingModel): Rating of the feedback
            reviewer (UserModel): User that gave the feedback
            post (PostModel, optional): Post the feedback belongs to. 
            reviewed_feedback (FeedbackModel, optional): Feedback that the feedback was given on (response). Defaults to None.
        """
        self.description = description
        self.aspect = aspect
        self.rating = rating
        self.reviewer = reviewer
        self.post = post
        self.reviewed_feedback = reviewed_feedback
        super().__init__()
