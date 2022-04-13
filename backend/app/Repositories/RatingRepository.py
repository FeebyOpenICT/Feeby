from typing import List, Optional
from sqlalchemy.orm import Session

from Models import RatingModel


class RatingRepository:
    @staticmethod
    def get_all_ratings(db: Session) -> List[RatingModel]:
        """
        Gets aspect rating object mappings from db

        returns a list of aspect rating mapped classes, returns an empty list if none are found
        """
        db_aspect_ratings = db.query(
            RatingModel).order_by(RatingModel.title).all()
        return db_aspect_ratings

    @staticmethod
    def get_rating_by_id(id: int, db: Session) -> Optional[RatingModel]:
        """
        Get rating object mapping from db

        return rating mapped object class
        """
        rating = db.query(RatingModel).filter(
            RatingModel.id == id).first()

        return rating

    @staticmethod
    def create_rating(db: Session, title: str, description: str, short_description: str) -> RatingModel:
        rating = RatingModel(
            title=title, short_description=short_description, description=description)

        db.add(rating)
        db.commit()

        return rating
