from typing import List, Optional
from Exceptions import UnexpectedInstanceError
from Models import AspectModel, RatingModel
from sqlalchemy.orm import Session


class AspectRepository:
    @staticmethod
    def get_all_aspects(db: Session) -> List[AspectModel]:
        """get all aspects from database

        Args:
            db (Session): database session

        Returns:
            List[AspectModel]: list of aspects from database
        """
        db_aspects = db.query(AspectModel).order_by(AspectModel.title).all()
        return db_aspects

    @staticmethod
    def get_aspect_by_id(id: int, db: Session) -> Optional[AspectModel]:
        """Get aspect from database by id

        Args:
            id (int): id of aspect in database
            db (Session): database session

        Returns:
            Optional[AspectModel]: returns either aspect from database or None
        """
        db_aspect = db.query(AspectModel).filter(AspectModel.id == id).first()

        return db_aspect

    @staticmethod
    def save(
        aspect: AspectModel,
        db: Session
    ) -> AspectModel:
        """Create aspect in db

        Args:
            aspect (AspectModel): aspect
            db (Session): database session

        Raises:
            UnexpectedInstance: if instance is not of AspectModel

        Returns:
            AspectModel: newly created aspect from database
        """
        if not isinstance(aspect, AspectModel):
            raise UnexpectedInstanceError

        db.add(aspect)
        db.commit()

        return aspect
