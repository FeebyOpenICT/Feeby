from fastapi import APIRouter, Depends, Security
from Models.Aspect import Aspect
from typing import List
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Models.AspectRating import AspectRating
from Schemas.AspectRating import AspectRatingInDB, CreateAspectRating
from database import get_db_connection
from Models.Role import Roles
from Models.User import User

router = APIRouter(
    prefix="/ratings",
    tags=["Aspect ratings"]
)


@router.get('/', response_model=List[AspectRatingInDB])
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
    Read all Aspects Ratings

    Allowed roles: admin, instructor, content_developer, teaching_assistant, student
    """
    all_aspect_ratings = AspectRating.get_aspect_ratings(db)
    return all_aspect_ratings


@router.post('/', response_model=AspectRatingInDB)
async def aspect(
        body: CreateAspectRating,
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
    Create aspect rating

    Allowed roles: admin, instructor
    """
    aspect_rating = AspectRating(
        title=body.title,
        short_description=body.short_description,
        description=body.description,
    )
    aspect_rating.save_self(db)
    return aspect_rating
