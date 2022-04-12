from tkinter import E
from typing import List
from Models import AspectModel, RatingModel
from sqlalchemy.orm import Session


class AspectRepository:
    @staticmethod
    def get_all_aspects(db: Session) -> List[AspectModel]:
        """
        Gets aspect object mappings from db

        returns a list of aspect mapped classes, returns an empty list if none are found
        """
        db_aspects = db.query(AspectModel).order_by(AspectModel.title).all()
        return db_aspects

    @staticmethod
    def get_aspect_by_id(id: int, db: Session) -> AspectModel:
        """
        Gets post object mapping from db
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
        db.add(aspect)
        db.commit()
        db.refresh(aspect)
        return aspect
