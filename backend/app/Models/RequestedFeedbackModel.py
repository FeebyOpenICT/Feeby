import uuid as uuid

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base
from . import UserModel
from .RevisionModel import RevisionModel


class RequestedFeedbackModel(Base):
    """RequestedFeedbackModel
    """
    __tablename__ = 'requested_feedback'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    time_created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    time_opened = Column(DateTime(timezone=True))
    time_finished = Column(DateTime(timezone=True))

    revision_id = Column(Integer, ForeignKey('revision.id'), primary_key=True, nullable=False)
    revision = relationship('RevisionModel')

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=False)
    user = relationship('UserModel')

    def __init__(self, revision: RevisionModel, user: UserModel):
        """RequestedFeedbackModel constructor

        Args:
            revision (RevisionModel): Revision that feedback has been requested on
            user (UserModel): user that feedback has been requested from
        """
        self.revision = revision
        self.user = user
        super().__init__()
