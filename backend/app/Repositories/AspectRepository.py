from typing import List, Optional
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
    def create_aspect(
        title: str,
        short_description: str,
        description: str,
        external_url: str,
        ratings: List[RatingModel],
        db: Session
    ) -> AspectModel:
        """Create aspect in db

        Args:
            title (str): title of aspect
            short_description (str): short description of aspect, should fit inside tooltip
            description (str): description of aspect
            external_url (str): external url pointing to extra explanation of aspect
            ratings (List[RatingModel]): list of ratings from database
            db (Session): database session

        Returns:
            AspectModel: newly created aspect from database
        """
        aspect = AspectModel(
            title=title,
            short_description=short_description,
            description=description,
            external_url=external_url,
            ratings=ratings
        )

        db.add(aspect)
        db.commit()

        return aspect

    @staticmethod
    def update_aspect(
        aspect: AspectModel,
        db: Session
    ) -> AspectModel:
        """update aspect in database

        Args:
            aspect (AspectModel): aspect model with updated attributes that needs to be saved in database
            db (Session): database session 

        Returns:
            AspectModel: aspect as newly updated in database
        """
        db.add(aspect)
        db.commit()
        db.refresh(aspect)
        return aspect
