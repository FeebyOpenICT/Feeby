from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base
from .UserModel import UserModel


class PostModel(Base):
    """PostModel
    """
    __tablename__ = 'post'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, index=True)
    description: str = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('UserModel')

    revisions = relationship('RevisionModel', back_populates="post")

    def __init__(self, title: str, description: str, user: UserModel) -> None:
        """PostModel constructor

        Args:
            title (str): title of the post
            description (str): description of the post
            user (UserModel): User that created the post
        """
        self.title = title
        self.description = description
        self.user = user
        super().__init__()
