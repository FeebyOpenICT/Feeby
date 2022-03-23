from fastapi import APIRouter, Depends, Security, status
from Models.Aspect import Aspect
from typing import List
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas.Aspect import CreateAspect, AspectInDB
from database import get_db_connection
from Models.Role import Roles
from Models.User import User
from Models.Rating import Rating

router = APIRouter(
    prefix="/aspects",
    tags=["Aspects"]
)


@router.get('/', response_model=List[AspectInDB])
async def get_aspects(
        current_active_user: User = Security(
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
    all_aspects = Aspect.get_all_aspects(db)
    return all_aspects


@router.post('/', response_model=AspectInDB, status_code=status.HTTP_201_CREATED)
async def aspect(
        body: CreateAspect,
        current_active_user: User = Security(
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
    ratings = [Rating.get_rating_by_id(rating_id=rating_id, db=db)
               for rating_id in body.rating_ids]

    aspect = Aspect(
        title=body.title,
        short_description=body.short_description,
        description=body.description,
        external_url=body.external_url,
        ratings=ratings
    )

    aspect.save_self(db)

    return aspect
