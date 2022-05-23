from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from typing import Optional

from .RevisionModel import RevisionModel
from .FeedbackModel import FeedbackModel
from database import Base


class FileModel(Base):
    """FileModel
    """
    __tablename__ = 'file'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    filename: str = Column(String(length=255), nullable=False, index=True)
    content_type: str = Column(String(length=255), nullable=False)
    location: str = Column(String(length=255), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    revision_id = Column(Integer, ForeignKey('revision.id'), nullable=True)
    revision = relationship('RevisionModel')

    feedback_id = Column(Integer, ForeignKey('feedback.id'), nullable=True)
    feedback = relationship('FeedbackModel')

    def __init__(self, filename: str, content_type: str, location: str, revision: RevisionModel, feedback: FeedbackModel) -> None:
        """FileModel constructor

        Args:
            filename (str): name of the file
            content_type (str): content type of the file
            location (str): location of the file
            revision (RevisionModel): revision file might have been added to
            feedback (FeedbackModel): feedback file might have been added to
        """
        self.filename = filename
        self.content_type = content_type
        self.location = location
        self.revision = revision
        self.feedback = feedback
        super().__init__()
