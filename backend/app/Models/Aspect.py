from pickletools import read_stringnl_noescape
from typing import List
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session, relationship
from sqlalchemy.sql import func
from Exceptions.NotFound import NotFound

from Models.Rating import RatingModel
from database import Base
from .SaveableModel import SaveableModel


class AspectModel(Base, SaveableModel):
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

    rating_ids = relationship("RatingModel", secondary='aspect_rating')

    def __init__(self, title: str, short_description: str, description: str, external_url: str, ratings: List[RatingModel]) -> None:
        self.title = title
        self.short_description = short_description
        self.description = description
        self.external_url = external_url
        if len(ratings) == 0:
            raise ValueError("ratings may not be empty")
        self.rating_ids = ratings
        super().__init__()

    # static not class method because I want it to always return an Aspect instance
    @staticmethod
    def get_all_aspects(db: Session):
        """
        Gets aspect object mappings from db

        returns a list of aspect mapped classes, returns an empty list if none are found
        """
        db_aspects = db.query(AspectModel).order_by(AspectModel.title).all()
        return db_aspects

    # static not class method because I want it to always return a aspect instance
    @staticmethod
    def get_aspect_by_id(id: int, db: Session):
        """
        Gets post object mapping from db
        """
        db_aspect = db.query(AspectModel).filter(AspectModel.id == id).first()
        if not db_aspect:
            raise NotFound(f"aspect")
        return db_aspect

