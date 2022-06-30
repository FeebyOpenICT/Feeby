from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from database import Base
from .PostModel import PostModel


class RevisionModel(Base):
    __tablename__ = 'revision'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    description: str = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship("PostModel", back_populates="revisions")

    feedback = relationship("FeedbackModel")

    requests = relationship("RequestedFeedbackModel")

    def __init__(self, description: str, post: PostModel) -> None:
        self.description = description
        self.post = post
        super().__init__()
