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

    Allowed roles: admin, instructor
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


@router.patch('/{aspect_id}', response_model=List[AspectUpdate], status_code=status.HTTP_200_OK)
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
    with Session(db) as session:
        db_aspect = session.get(body, aspect_id)
        if not db_aspect:
            raise HTTPException(status_code=404, detail="aspect not found")
        aspect_data = body.dict(exclude_unset=True)
        for key, value in aspect_data.items():
            setattr(db_aspect, key, value)

    ratings = [RatingModel.get_rating_by_id(rating_id=rating_id, db=db)
               for rating_id in body.rating_ids]

    aspect.save_self(db)

    return aspect
