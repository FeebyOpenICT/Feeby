from typing import List
from requests import Session
from sqlalchemy.orm import Session
from Models import RatingModel
from Repositories import RatingRepository


class RatingService:
    @staticmethod
    def get_all_aspect_ratings(db: Session) -> List[RatingModel]:
        all_ratings = RatingRepository.get_all_aspect_ratings(db=db)
        return all_ratings

    @staticmethod
    def create_rating(db: Session, title: str, description: str, short_description: str) -> RatingModel:
        rating = RatingRepository.create_rating(
            db=db, title=title, short_description=short_description, description=description)
        return rating
