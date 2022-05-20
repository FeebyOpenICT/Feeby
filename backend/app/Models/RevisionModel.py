from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from .PostModel import PostModel


class RevisionModel(Base):
    """RevisionModel
    """
    __tablename__ = 'revision'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship("PostModel", back_populates="revisions")

    def __init__(self, description: str, post: PostModel):
        """RevisionModel initializer

        Args:
            description (str): description of revision
            post (PostModel): post that new revision will belong to
        """
        self.description = description
        self.post = post
