from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Exceptions import NotFoundException
from Models import AspectModel, RatingModel
# circular import fix
from Services.RatingService import RatingService
from Repositories import AspectRepository
from Schemas import UpdateAspect


class AspectService:
    def get_all_aspects(
        db: Session
    ) -> List[AspectModel]:
        """Get all aspects

        Args:
            db (Session): database session

        Returns:
            List[AspectModel]: list of aspects
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
        """Create aspect whilst also verifying ratings

        Args:
            title (str): title of aspect
            short_description (str): short description of aspect, should fit within tooltip
            description (str): description of aspect
            external_url (str): external url pointing to extra info about aspect
            rating_ids (List[int]): list of int ids of ratings that are saved in the database
            db (Session): database session

        Raises:
            NotFound: if rating is not found it will raise a not found error on that rating

        Returns:
            AspectModel: newly created aspect
        """
        ratings: List[RatingModel] = []

        for id in rating_ids:
            rating = RatingService.get_rating_by_id(db=db, id=id)

            if rating is None:
                raise NotFoundException(resource="rating", id=id)

            ratings.append(rating)

        aspect = AspectRepository.save(
            aspect=AspectModel(title=title, description=description,
                               short_description=short_description, external_url=external_url, ratings=ratings),
            db=db
        )

        return aspect

    def patch_aspect(
            aspect_id: int,
            body: UpdateAspect,
            db: Session
    ) -> AspectModel:
        """patch aspect whilst verifying if aspect exists and if new rating ids exist

        Args:
            aspect_id (int): id of aspect as saved in database
            body (UpdateAspect): new attributes of aspect, all optional see Schema
            db (Session): database session

        Raises:
            NotFound: if aspect or ratings are not found
            HTTPException: if ratings are empty list

        Returns:
            AspectModel: updated aspect as saved in database
        """
        aspect = AspectRepository.get_aspect_by_id(aspect_id, db)

        if aspect is None:
            raise NotFoundException(id=aspect_id, resource="aspect")

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

        aspect = AspectRepository.save(aspect=aspect, db=db)

        return aspect
