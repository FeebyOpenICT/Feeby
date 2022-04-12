from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Exceptions import NotFound
from Models import AspectModel, RatingModel
from Services import RatingService
from Repositories import AspectRepository
from Schemas import UpdateAspect


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
        title: str,
        short_description: str,
        description: str,
        external_url: str,
        rating_ids: List[int],
        db: Session
    ) -> AspectModel:
        """
        Create aspect
        """
        ratings: List[RatingModel] = []

        for id in rating_ids:
            rating = RatingService.get_rating_by_id(id=id, db=db)

            if rating is None:
                raise NotFound(resource="rating", id=id)

            ratings.append(rating)

        aspect = AspectRepository.create_aspect(
            title=title,
            short_description=short_description,
            description=description,
            external_url=external_url,
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
        aspect = AspectRepository.get_aspect_by_id(aspect_id, db)

        if aspect is None:
            raise NotFound(id=aspect_id, resource="aspect")

        aspect_data = body.dict(exclude_unset=True)

        if "rating_ids" in aspect_data:
            if len(aspect_data["rating_ids"]) > 0:
                ratings = [RatingModel.get_rating_by_id(rating_id=rating_id, db=db)
                           for rating_id in aspect_data.pop("rating_ids")]
                setattr(aspect, "ratings", ratings)
            else:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="No rating")

        for key, value in aspect_data.items():
            setattr(aspect, key, value)

        aspect = AspectRepository.update_aspect(aspect=aspect, db=db)

        return aspect
