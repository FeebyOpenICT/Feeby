from Models.UserModel import UserModel
from Schemas.RolesSchema import RolesEnum
from database import get_db_connection
from Schemas.Rating import RatingInDB, CreateRating
from Models.Rating import RatingModel
from sqlalchemy.orm import Session
from Auth.validate_user import get_current_active_user
from typing import List
from fastapi import APIRouter, Depends, Security, status

router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"]
)


@router.get('/', response_model=List[RatingInDB])
async def get_ratings(
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
                RolesEnum.STUDENT,
                RolesEnum.ADMIN,
                RolesEnum.INSTRUCTOR,
                RolesEnum.CONTENT_DEVELOPER,
                RolesEnum.TEACHING_ASSISTANT,
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """
    Read all Aspects Ratings

    Allowed roles: admin, instructor, content_developer, teaching_assistant, student
    """
    all_aspect_ratings = RatingModel.get_all_aspect_ratings(db)
    return all_aspect_ratings


@router.post('/', response_model=RatingInDB, status_code=status.HTTP_201_CREATED)
async def create_aspect(
        body: CreateRating,
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
                RolesEnum.ADMIN,
                RolesEnum.INSTRUCTOR,
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """
    Create aspect rating

    Allowed roles: admin, instructor
    """
    aspect_rating = RatingModel(
        title=body.title,
        short_description=body.short_description,
        description=body.description,
    )
    aspect_rating.save_self(db)
    return aspect_rating
