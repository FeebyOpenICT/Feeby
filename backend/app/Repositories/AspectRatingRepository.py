from typing import Optional
from sqlalchemy import and_
from sqlalchemy.orm import Session
from .RepositoryBase import RepositoryBase
from Models import AspectRatingModel


class AspectRatingRepository(RepositoryBase):
    def get_by_id(aspect_id: int, rating_id: int, db: Session) -> Optional[AspectRatingModel]:
        """Get aspect_rating by id

         Args:
             aspect_id (int): id of aspect
             rating_id (int): id of rating
             db (Session): database session

         Returns:
             Optional[AspectRatingModel]: if aspect and rating are coupled it will return the AspectRatingModel
         """
        result = db.query(AspectRatingModel).filter(
            and_(
                AspectRatingModel.aspect_id == aspect_id,
                AspectRatingModel.rating_id == rating_id
            )
        ).first()
        return result
