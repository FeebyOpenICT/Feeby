from sqlalchemy.orm import Session
from Exceptions import NotFoundException
from Models import AspectRatingModel
from Repositories import AspectRatingRepository


class AspectRatingService:
    @staticmethod
    def get_aspect_rating_or_fail(aspect_id: int, rating_id: int, db: Session) -> AspectRatingModel:
        """get aspect rating by id or fail

        Args:
            aspect_id (int): id of aspect as saved im database
            rating_id (int): id of rating as saved im database
            db (Session): database session

        Raises:
            NotFoundException: If rating is not a part of aspect throw not found

        Returns:
            AspectRatingModel: aspect rating 
        """
        aspect_rating = AspectRatingRepository.get_by_id(
            aspect_id=aspect_id, rating_id=rating_id, db=db)

        if not aspect_rating:
            raise NotFoundException(
                "aspect_rating", f'{aspect_id}:{rating_id}')

        return aspect_rating
