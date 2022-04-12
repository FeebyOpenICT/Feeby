from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Exceptions import NotFound
from Models import AspectModel, RatingModel

from Repositories import AspectRepository
from Schemas import CreateAspect, UpdateAspect


class AspectService:
    def get_all_aspects(
        db: Session
    ) -> List[AspectModel]:
        """
        Get all Aspects
        """
        all_aspects = AspectRepository.get_all_aspects(db)
        return all_aspects

    def create_aspect(
            body: CreateAspect,
            db: Session
    ) -> AspectModel:
        """
        Create aspect
        """
        ratings = [RatingModel.get_rating_by_id(rating_id=rating_id, db=db)
                   for rating_id in body.rating_ids]

        aspect = AspectRepository.create_aspect(
            title=body.title,
            short_description=body.short_description,
            description=body.description,
            external_url=body.external_url,
            ratings=ratings,
            db=db
        )

        return aspect

    def patch_aspect(
            aspect_id: int,
            body: UpdateAspect,
            db: Session
    ) -> AspectModel:
        """
        Update aspect
        """
        db_aspect = AspectRepository.get_aspect_by_id(aspect_id, db)

        if not db_aspect:
            raise NotFound(id=aspect_id, resource="aspect")

        aspect_data = body.dict(exclude_unset=True)

        if "rating_ids" in aspect_data:
            if len(aspect_data["rating_ids"]) > 0:
                ratings = [RatingModel.get_rating_by_id(rating_id=rating_id, db=db)
                           for rating_id in aspect_data.pop("rating_ids")]
                setattr(db_aspect, "ratings", ratings)
            else:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="No rating")

        for key, value in aspect_data.items():
            setattr(db_aspect, key, value)

        db_aspect = AspectRepository.update_aspect(aspect=db_aspect, db=db)

        return db_aspect
