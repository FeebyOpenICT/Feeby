from typing import List, Optional
from sqlalchemy.orm import Session

from Models import RatingModel


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
    def create_rating(db: Session, title: str, description: str, short_description: str) -> RatingModel:
        """create rating in database

        Args:
            db (Session): database session
            title (str): title of rating
            description (str): description of rating
            short_description (str): short description of rating, should fit inside tooltip

        Returns:
            RatingModel: newly created rating as saved in database
        """
        rating = RatingModel(
            title=title, short_description=short_description, description=description)

        db.add(rating)
        db.commit()

        return rating
