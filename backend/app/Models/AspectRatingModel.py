from Models.AspectModel import AspectModel
from Models.RatingModel import RatingModel
from database import Base
from sqlalchemy import DateTime, Integer, Column, ForeignKey, func
from sqlalchemy.orm import relationship


class AspectRatingModel(Base):
    """AspectRatingModel
    """
    __tablename__ = 'aspect_rating'

    aspect_id = Column(Integer, ForeignKey('aspect.id'), primary_key=True)
    aspect = relationship("AspectModel", backref="aspect_rating")

    rating_id = Column(Integer, ForeignKey('rating.id'), primary_key=True)
    rating = relationship("RatingModel", backref="aspect_rating")

    time_created = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, aspect: AspectModel, rating: RatingModel) -> None:
        """AspectRatingModel constructor

        Args:
            aspect (AspectModel): aspect that rating will belong to
            rating (RatingModel): rating that will belong to aspect
        """
        self.aspect = aspect
        self.rating = rating
