from typing import List, Optional
from requests import Session
from sqlalchemy.orm import Session
from Exceptions import NotFoundException
from Models import RatingModel
from Repositories import RatingRepository


class RatingService:
    @staticmethod
    def get_all_ratings(db: Session) -> List[RatingModel]:
        """Get all ratings

        Args:
            db (Session): database session

        Returns:
            List[RatingModel]: list of all ratings
        """
        all_ratings = RatingRepository.get_all_ratings(db=db)
        return all_ratings

    @staticmethod
    def get_rating_by_id_or_fail(db: Session, id: int) -> RatingModel:
        """Get rating by id or raise NotFound

        Args:
            db (Session): database session
            id (int): id of rating

        Returns:
            RatingModel: rating as saved in database
        """
        rating = RatingRepository.get_rating_by_id(id=id, db=db)

        if not rating:
            raise NotFoundException(resource="rating", id=id)

        return rating

    @staticmethod
    def create_rating(db: Session, title: str, description: str, short_description: str) -> RatingModel:
        """Create rating

        Args:
            db (Session): database session
            title (str): title of rating
            description (str): description of rating
            short_description (str): short description of rating, should fit inside tooltip

        Returns:
            RatingModel: newly created rating
        """
        rating = RatingRepository.save(rating=RatingModel(title=title, short_description=short_description, description=description),
                                       db=db)
        return rating
