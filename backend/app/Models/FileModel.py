from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .PostModel import PostModel
from database import Base


class FileModel(Base):
    """FileModel
    """
    __tablename__ = 'file'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    filename: str = Column(String(length=255), nullable=False, index=True)
    content_type: str = Column(String(length=200), nullable=False)
    location: str = Column(String(length=200), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship('PostModel')

    def __init__(self, filename: str, content_type: str, location: str, post: PostModel) -> None:
        """FileModel constructor

        Args:
            filename (str): name of the file
            content_type (str): content type of the file
            location (str): location of the file
            post (PostModel): post file has been added to
        """
        self.filename = filename
        self.content_type = content_type
        self.location = location
        self.post = post
        super().__init__()
