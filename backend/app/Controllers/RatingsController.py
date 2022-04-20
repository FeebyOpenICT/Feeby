from Models import UserModel
from Schemas import RolesEnum, RatingInDB, CreateRating, RatingUpdate
from database import get_db_connection
from sqlalchemy.orm import Session
from Auth.validate_user import get_current_active_user
from typing import List
from fastapi import APIRouter, Depends, Security, status
from Services import RatingService

router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"]
)


@router.get('', response_model=List[RatingInDB])
async def get_all_ratings(
        current_active_user: UserModel = Depends(get_current_active_user),
        db: Session = Depends(get_db_connection)
):
    """Get all ratings

    Allowed roles:
    - All
    """
    all_ratings = RatingService.get_all_ratings(db=db)
    return all_ratings


@router.post('', response_model=RatingInDB, status_code=status.HTTP_201_CREATED)
async def create_rating(
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
    """Create rating

    Allowed roles:
    - All
    """
    rating = RatingService.create_rating(
        title=body.title,
        short_description=body.short_description,
        description=body.description,
        db=db
    )
    return rating


@router.patch('/{rating_id}', response_model=RatingInDB, status_code=status.HTTP_200_OK)
async def patch_aspect(
        rating_id: int,
        body: RatingUpdate,
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
    Update rating

    Allowed roles: admin, instructor
    """
    rating = RatingService.patch_rating(rating_id=rating_id, body=body, db=db)
    return rating
