from sqlalchemy import and_
from sqlalchemy.orm import Session
from .RepositoryBase import RepositoryBase
from Models import AspectRatingModel


class AspectRatingRepository(RepositoryBase):
    def get_by_id(aspect_id: int, rating_id: int, db: Session):
        result = db.query(AspectRatingModel).filter(
            and_(
                AspectRatingModel == aspect_id,
                AspectRatingModel == rating_id
            )
        ).first()
        return result
