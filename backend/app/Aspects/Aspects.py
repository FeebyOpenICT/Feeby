from fastapi import APIRouter, Depends, Security, status, HTTPException
from Models.Aspect import AspectModel
from typing import List
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas.Aspect import CreateAspect, AspectInDB, AspectUpdate
from database import get_db_connection
from Models.Role import Roles
from Models.User import UserModel
from Models.Rating import RatingModel

router = APIRouter(
    prefix="/aspects",
    tags=["Aspects"]
)


@router.get('/', response_model=List[AspectInDB])
async def get_aspects(
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
                Roles.STUDENT['title'],
                Roles.ADMIN['title'],
                Roles.INSTRUCTOR['title'],
                Roles.CONTENT_DEVELOPER['title'],
                Roles.TEACHING_ASSISTANT['title'],
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """
    Read all Aspects

    Allowed roles: admin, instructor, student, content-developer, teaching-assistant
    """
    all_aspects = AspectModel.get_all_aspects(db)
    return all_aspects


@router.post('/', response_model=AspectInDB, status_code=status.HTTP_201_CREATED)
async def aspect(
        body: CreateAspect,
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
                Roles.ADMIN['title'],
                Roles.INSTRUCTOR['title'],
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """
    Create aspect

    Allowed roles: admin, instructor
    """
    ratings = [RatingModel.get_rating_by_id(rating_id=rating_id, db=db)
               for rating_id in body.rating_ids]

    aspect = AspectModel(
        title=body.title,
        short_description=body.short_description,
        description=body.description,
        external_url=body.external_url,
        ratings=ratings
    )

    aspect.save_self(db)

    return aspect


@router.patch('/{aspect_id}', response_model=AspectInDB, status_code=status.HTTP_200_OK)
async def patch_aspect(
        aspect_id: int,
        body: AspectUpdate,
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
                Roles.ADMIN['title'],
                Roles.INSTRUCTOR['title'],
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """
    Update aspect

    Allowed roles: admin, instructor
    """
    db_aspect = AspectModel.get_aspect_by_id(aspect_id, db)

    aspect_data = body.dict(exclude_unset=True)

    if "rating_ids" in aspect_data:
        if len(aspect_data["rating_ids"]) > 0:
            ratings = [RatingModel.get_rating_by_id(rating_id=rating_id, db=db)
                       for rating_id in aspect_data.pop("rating_ids")]
            setattr(db_aspect, "ratings", ratings)
        else:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="No rating")

    for key, value in aspect_data.items():
        setattr(db_aspect, key, value)

    db_aspect.save_self(db)

    return db_aspect
