from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Session, relationship

from .SaveableModel import SaveableModel
from database import Base
from .UserModel import UserModel


class PostModel(Base, SaveableModel):
    """
    Mapped Post class

    Represents a post in the database
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

    def __init__(self, title, description, user: UserModel) -> None:
        self.title = title
        self.description = description
        self.user = user
        super().__init__()