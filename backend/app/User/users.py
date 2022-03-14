from fastapi import APIRouter, Depends
from Auth.validate_user import get_current_active_user
from Models.User import User
from Schemas.User import GetUser

router = APIRouter(
  prefix="/users",
  tags=["Users"]
)

@router.get('/self', response_model=GetUser)
async def read_users_me(current_active_user: User = Depends(get_current_active_user)):
  return current_active_user
