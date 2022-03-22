from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from Models.SaveableModel import SaveableModel

from .Aspect import Base


class AspectRating(Base, SaveableModel):
    """
    Mapped Aspect class

    Represents an aspect in the database
    """
    __tablename__ = 'aspect_rating'

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, index=True)
    short_description: str = Column(String(length=255), nullable=False)
    description: str = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    # static not class method because I want it to always return an Aspect instance
    @staticmethod
    def get_all_aspect_ratings(db: Session):
        """
        Gets aspect rating object mappings from db

        returns a list of aspect rating mapped classes, returns an empty list if none are found
        """
        db_aspect_ratings = db.query(
            AspectRating).order_by(AspectRating.title).all()
        return db_aspect_ratings
