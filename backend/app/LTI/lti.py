from fastapi import APIRouter, Form, Depends
from sqlalchemy.orm import Session

from Auth.redir_to_auth import redir_to_oauth
from Models.User import User
from Models.Role import Role
from database import get_db_connection

router = APIRouter(
  prefix="/lti",
  tags=["L.T.I."]
)

@router.post('/launch')
async def launch(
  # user_id: str = Form(...),
  # ext_roles: str = Form(...),
  # roles: str = Form(...),
  # db: Session = Depends(get_db_connection)
):
  """
  Launch call for canvas
  
  Always redir to oauth of canvas, skips me having to implement lti validation or having the possibility of having any security leaks
  """
  # TODO check if user has access and or refresh tokens, if they do check them and if not send them to oauth
  return redir_to_oauth()
  # # check if user is already in our db, if they are we already have the refresh and or auth tokens
  # user = db.query(User).filter(User.canvas_id == user_id).first()
  # if user and user.refresh_token: 
  #   # user has logged in before
  #   return user
  # else:
  #   # TODO get role
  #   user = User(canvas_id=user_id, role=Role.get_admin_role(db))
