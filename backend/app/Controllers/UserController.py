from fastapi import APIRouter, Security, Depends
from sqlalchemy.orm import Session
from Auth.validate_user import get_current_active_user
from Exceptions.NotFound import NotFound
from Models.User import UserModel
from Schemas.UserSchema import UserPublicSearch, UserInDB
from Models.Role import Roles
from Services.UserService import UserService
from database import get_db_connection
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get('', response_model=List[UserPublicSearch])
async def search_through_users(
    search: str = '',
    db: Session = Depends(get_db_connection),
    current_active_user: UserModel = Depends(get_current_active_user)
):
    """
    Get and or search through users

    Gets the internal id, canvas_email and fullname

    Allowed roles: all
    """
    users = UserService.get_user_ids_by_name_or_email(query=search, db=db)
    return users


@router.get('/self', response_model=UserInDB)
async def get_user_self(
    current_active_user: UserModel = Depends(get_current_active_user)
):
    """
    Gets current active user

    Allowed roles: all
    """
    # already throws unauthenticated if the user is not logged in so no further error handling necessary
    return current_active_user


@router.get('/{user_id}', response_model=UserInDB)
async def get_user_by_id(
    user_id: int,
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
    Gets specific user by id

    Allowed roles: admin, instructor
    """
    user = UserService.get_user_by_id(user_id, db)

    if not user:
        raise NotFound("user", user_id)

    return user


@router.get('/canvas/{user_id}', response_model=UserInDB)
async def get_user_by_canvas_id(
    user_id: int,
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
    Gets specific user by their canvas id

    Allowed roles: admin, instructor
    """
    user = UserService.get_user_by_canvas_id(user_id, db)

    if not user:
        raise NotFound("user", user_id)

    return user
