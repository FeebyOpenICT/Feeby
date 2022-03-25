from typing import Any
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from Exceptions.NotFound import NotFound

from Models.SaveableModel import SaveableModel

from .Post import Base


class Rating(Base, SaveableModel):
    """
    Mapped Aspect class

    Represents an aspect in the database
    """
    __tablename__ = 'rating'

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, index=True)
    short_description: str = Column(String(length=255), nullable=False)
    description: str = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    def __init__(self, title: str, short_description: str, description: str,) -> None:
        self.title = title
        self.short_description = short_description
        self.description = description
        super().__init__()

    # static not class method because I want it to always return an Aspect instance
    @staticmethod
    def get_all_aspect_ratings(db: Session):
        """
        Gets aspect rating object mappings from db

        returns a list of aspect rating mapped classes, returns an empty list if none are found
        """
        db_aspect_ratings = db.query(
            Rating).order_by(Rating.title).all()
        return db_aspect_ratings

    @staticmethod
    def get_rating_by_id(rating_id: int, db: Session):
        """
        Get rating object mapping from db

        return rating mapped object class
        """
        rating = db.query(Rating).filter(Rating.id == rating_id).first()

        if not rating:
            raise NotFound(f"rating: {rating_id}")

        return rating
