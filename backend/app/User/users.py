from fastapi import APIRouter, Security, Depends
from sqlalchemy.orm import Session
from Auth.validate_user import get_current_active_user
from Models.User import User
from Schemas.User import UserInDB
from Models.Role import Roles
from database import get_db_connection

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

@router.get('/self', response_model=UserInDB)
async def get_user_self(
  current_active_user: User = Security(
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
  Gets specific user by id

  Allowed roles: admin, instructor
  """
  user = User.get_user_by_id(user_id, db)
  return user


@router.get('/canvas/{user_id}', response_model=UserInDB)
async def get_user_by_canvas_id(
  user_id: int,
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
  Gets specific user by their canvas id

  Allowed roles: admin, instructor
  """
  user = User.get_user_by_canvas_id(user_id, db)
  return user
