from typing import List, Optional
from sqlalchemy.orm import Session

from Models import RatingModel
from Exceptions import UnexpectedInstanceError


class RatingRepository:
    @staticmethod
    def get_all_ratings(db: Session) -> List[RatingModel]:
        """Get all ratings from database

        Args:
            db (Session): database session

        Returns:
            List[RatingModel]: list of all ratings from database
        """
        db_aspect_ratings = db.query(
            RatingModel).order_by(RatingModel.title).all()
        return db_aspect_ratings

    @staticmethod
    def get_rating_by_id(id: int, db: Session) -> Optional[RatingModel]:
        """Get a rating from the database by id

        Args:
            id (int): id of rating as saved in database
            db (Session): database session

        Returns:
            Optional[RatingModel]: rating as saved in database or None
        """
        rating = db.query(RatingModel).filter(
            RatingModel.id == id).first()

        return rating

    @staticmethod
    def save(rating: RatingModel, db: Session) -> RatingModel:
        """Save rating instance in database

        Args:
            rating (RatingModel): rating model
            db (Session): database session

        Raises:
            UnexpectedInstanceError: if rating is not RatingModel instance

        Returns:
            RatingModel: rating as saved in database
        """
        if not isinstance(rating, RatingModel):
            raise UnexpectedInstanceError

        db.add(rating)

        return rating
