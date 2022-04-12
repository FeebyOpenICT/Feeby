from typing import List
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from Models.Rating import RatingModel
from database import Base


class AspectModel(Base):
    """
    Mapped Aspect class

    Represents an aspect in the database
    """
    __tablename__ = 'aspect'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, index=True)
    short_description: str = Column(String(length=255), nullable=False)
    description: str = Column(String(length=1000), nullable=False)
    external_url: str = Column(String(length=2000), nullable=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    ratings = relationship("RatingModel", secondary='aspect_rating')

    def __init__(self, title: str, short_description: str, description: str, external_url: str, ratings: List[RatingModel]) -> None:
        self.title = title
        self.short_description = short_description
        self.description = description
        self.external_url = external_url
        if len(ratings) == 0:
            raise ValueError("ratings may not be empty")
        self.ratings = ratings
        super().__init__()
