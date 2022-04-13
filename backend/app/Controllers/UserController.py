from fastapi import APIRouter, Security, Depends
from sqlalchemy.orm import Session
from Auth.validate_user import get_current_active_user
from Exceptions.NotFound import NotFound
from Models.UserModel import UserModel
from Schemas.UserSchema import UserPublicSearch, UserInDB
from Schemas.RolesEnum import RolesEnum
from Services.UserService import UserService
from database import get_db_connection
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get('', response_model=List[UserPublicSearch])
async def search_through_users(
    q: str = '',
    db: Session = Depends(get_db_connection),
    current_active_user: UserModel = Depends(get_current_active_user)
):
    """Search through all active users in the database with public info

    Args:
        q (str, optional): search query term, defaults. Defaults to ''.

    Allowed roles:
    - All
    """
    users = UserService.get_user_ids_by_name_or_email(query=q, db=db)
    return users


@router.get('/self', response_model=UserInDB)
async def get_user_self(
    current_active_user: UserModel = Depends(get_current_active_user)
):
    """Get current self

    Allowed roles:
    - All
    """
    # already throws unauthenticated if the user is not logged in so no further error handling necessary
    return current_active_user


@router.get('/{user_id}', response_model=UserInDB)
async def get_user_by_id(
    user_id: int,
    current_active_user: UserModel = Security(
        get_current_active_user,
        scopes=[
        RolesEnum.ADMIN,
        RolesEnum.INSTRUCTOR,
        ]
    ),
    db: Session = Depends(get_db_connection)
):
    """Get user by id

    Allowed roles:
    - Admin
    - Instructor
    """
    user = UserService.get_user_by_id_or_fail(id=user_id, db=db)
    return user


@router.get('/{user_id}/canvas', response_model=UserInDB)
async def get_user_by_canvas_id(
    user_id: int,
    current_active_user: UserModel = Security(
        get_current_active_user,
        scopes=[
        RolesEnum.ADMIN,
        RolesEnum.INSTRUCTOR,
        ]
    ),
    db: Session = Depends(get_db_connection)
):
    """Get user by their canvas id

    Allowed roles:
    - Admin
    - Instructor
    """
    user = UserService.get_user_by_canvas_id_or_fail(user_id, db)
    return user
