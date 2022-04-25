from Models.RevisionModel import RevisionModel
from Models.UserModel import UserModel
from Models.RatingModel import RatingModel
from Models.AspectModel import AspectModel
from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship


class FeedbackModel(Base):
    __tablename__ = 'revision'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    rating_id = Column(Integer, ForeignKey('rating.id'), nullable=False)
    rating = relationship("RatingModel")

    aspect_id = Column(Integer, ForeignKey('aspect.id'), nullable=False)
    aspect = relationship("AspectModel")

    revision_id = Column(Integer, ForeignKey('revision.id'), nullable=False)
    revision = relationship("RevisionModel")

    reviewer_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    reviewer = relationship("UserModel")

    def __init__(self, description: str, rating: RatingModel, aspect: AspectModel, revision: RevisionModel, reviewer: UserModel) -> None:
        self.description = description
        self.rating = rating
        self.aspect = aspect
        self.revision = revision
        self.reviewer = reviewer
