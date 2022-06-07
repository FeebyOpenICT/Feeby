from sqlalchemy.orm import Session
from Exceptions import NotFoundException
from Repositories import AspectRatingRepository


class AspectRatingService:
    def get_aspect_rating_or_fail(aspect_id: int, rating_id: int, db: Session):
        aspect_rating = AspectRatingRepository.get_by_id(
            aspect_id=aspect_id, rating_id=rating_id, db=db)

        if not aspect_rating:
            raise NotFoundException(
                "aspect_rating", f'{aspect_id}:{rating_id}')

        return aspect_rating
