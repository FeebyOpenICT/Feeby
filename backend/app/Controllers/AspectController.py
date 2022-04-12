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
    """
    Read all Aspects
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
    """
    Create aspect

    Allowed roles: admin, instructor
    """
    aspect = AspectService.create_aspect(body=body, db=db)
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
    """
    Update aspect

    Allowed roles: admin, instructor
    """
    aspect = AspectService.patch_aspect(aspect_id=aspect_id, body=body, db=db)
    return aspect
