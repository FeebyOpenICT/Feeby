from fastapi import APIRouter, Depends, Security
from Models.Aspect import Aspect
from typing import List
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas.Aspect import CreateAspect
from database import get_db_connection
from Models.Role import Roles
from Models.User import User
from Schemas.Aspect import AspectInDB

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
    all_aspects = Aspect.get_aspects(db)
    return all_aspects


@router.post('/', response_model=AspectInDB)
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
    aspect = Aspect(
        title=body.title,
        short_description=body.short_description,
        description=body.description,
        external_url=body.external_url,
    )
    aspect.save_self(db)
    return aspect
