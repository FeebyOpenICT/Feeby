from typing import List, Optional
from requests import Session
from sqlalchemy.orm import Session
from Exceptions import NotFoundException
from Models import RatingModel
from Repositories import RatingRepository
from Schemas import RatingUpdate


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

    @staticmethod
    def patch_rating(
            rating_id: int,
            body: RatingUpdate,
            db: Session
    ) -> RatingModel:
        """patch rating whilst verifying if rating exists

        Args:
            rating_id (int): id of aspect as saved in database
            body (RatingUpdate): new attributes of aspect, all optional see Schema
            db (Session): database session

        Raises:
            NotFound: if rating is not found

        Returns:
            RatingModel: updated aspect as saved in database
        """
        db_rating = RatingService.get_rating_by_id_or_fail(db=db, id=rating_id)

        rating_data = body.dict(exclude_unset=True)

        for key, value in rating_data.items():
            setattr(db_rating, key, value)

        db_rating.save_self(db)

        return db_rating
