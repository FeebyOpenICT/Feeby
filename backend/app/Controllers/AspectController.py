from fastapi import APIRouter, Depends, Security, status
from typing import List
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas import CreateAspect, AspectInDB, UpdateAspect, RolesEnum
from Services import AspectService
from database import get_db_connection
from Models import UserModel


router = APIRouter(
    prefix="/aspects",
    tags=["Aspects"]
)


@router.get('', response_model=List[AspectInDB])
async def get_all_aspects(
        current_active_user: UserModel = Depends(get_current_active_user),
        db: Session = Depends(get_db_connection)
):
    """Get all aspects

    Allowed roles:
    - All
    """
    all_aspects = AspectService.get_all_aspects(db)
    return all_aspects


@router.post('', response_model=AspectInDB, status_code=status.HTTP_201_CREATED)
async def create_aspect(
        body: CreateAspect,
        db: Session = Depends(get_db_connection),
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
                RolesEnum.ADMIN,
                RolesEnum.INSTRUCTOR,
            ]
        ),
):
    """Create aspect

    Allowed roles:
    - Admin
    - Instructor
    """
    aspect = AspectService.create_aspect(title=body.title, short_description=body.short_description,
                                         description=body.description, external_url=body.external_url, rating_ids=body.rating_ids, db=db)
    return aspect


@router.patch('/{aspect_id}', response_model=AspectInDB, status_code=status.HTTP_200_OK)
async def patch_aspect(
        aspect_id: int,
        body: UpdateAspect,
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
                RolesEnum.ADMIN,
                RolesEnum.INSTRUCTOR,
            ]
        ),
        db: Session = Depends(get_db_connection)
):
    """Patch aspect

    Args:
        aspect_id (int): id of aspect as saved in database

    Allowed roles:
    - Admin
    - Instructor
    """
    aspect = AspectService.patch_aspect(aspect_id=aspect_id, body=body, db=db)
    return aspect
