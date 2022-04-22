from typing import List
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Models.PostModel import PostModel
from database import Base


class FileModel(Base):
    """FileModel
       """
    __tablename__ = 'file'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    location: str = Column(String(length=255), nullable=False, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship('PostModel')

    def __init__(self, location: str, post: PostModel) -> None:
        """FileModel constructor

        Args:
            location (str): location of the file
            post (PostModel): the post which the file had been added to
        """
        self.location = location
        self.post = post
        super().__init__()
