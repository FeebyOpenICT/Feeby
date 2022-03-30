from fastapi import APIRouter, Security, Depends
from sqlalchemy.orm import Session
from Auth.validate_user import get_current_active_user
from Models.User import UserModel
from Repositories.User import UserRepository
from Schemas.User import UserPublicSearch, UserInDB
from Models.Role import Roles
from database import get_db_connection
from typing import List, Tuple

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get('/search', response_model=List[UserPublicSearch])
async def search_through_users(
    query: str,
    db: Session = Depends(get_db_connection),
    current_active_user: UserModel = Depends(get_current_active_user)
):
    """
    Searches through users and gets their email, fullname and internal id

    Allowed roles: all
    """
    users = UserRepository.get_user_ids_by_name_or_email(query=query, db=db)
    return users


@router.get('/self', response_model=UserInDB)
async def get_user_self(
    current_active_user: UserModel = Security(
        get_current_active_user,
        scopes=[
        Roles.STUDENT['title'],
        Roles.ADMIN['title'],
        Roles.INSTRUCTOR['title'],
        Roles.CONTENT_DEVELOPER['title'],
        Roles.TEACHING_ASSISTANT['title'],
        Roles.OBSERVER['title'],
        Roles.MENTOR['title']
        ]
    )
):
    """
    Gets current active user

    Allowed roles: admin, instructor, student, content_developer, teaching_assistant, observer, mentor
    """
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
    user = UserRepository.get_user_by_id(user_id, db)
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
    user = UserRepository.get_user_by_canvas_id(user_id, db)
    return user
