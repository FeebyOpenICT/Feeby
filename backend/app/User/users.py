from fastapi import APIRouter, Depends, Security
from Auth.validate_user import get_current_active_user
from Models.User import User
from Schemas.User import UserInDB
from Models.Role import Roles

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

@router.get('/self', response_model=UserInDB)
async def read_users_me(
  current_active_user: User = Security(
    get_current_active_user, 
    scopes=[
      Roles.STUDENT['title'],
      Roles.ADMIN['title'],
      Roles.INSTRUCTOR['title'],
      Roles.CONTENT_DEVELOPER['title'],
      Roles.TEACHING_ASSISTANT['title'],
      Roles.OBSERVER['title'],
    ]
  )
):
  return current_active_user
