from sqlalchemy.orm import Session
from fastapi import Cookie, Depends, Request, Security, HTTPException
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from .redir_to_auth import redir_to_oauth


from .JWTToken import Token
from config import BASE_APP_API_URL, BASE_URL, JWT_SECRET, JWT_ALGORITHM
from Models.User import User
from database import get_db_connection

# automatically checks if there is a Bearer ... token in the Authorizaiton header
token_auth_scheme = HTTPBearer()


async def get_current_user(jwt_token: HTTPAuthorizationCredentials = Depends(token_auth_scheme), db: Session = Depends(get_db_connection)):
  """
  Gets the current user from the database by decoding the jwt bearer token

  Returns the User mapped class
  """
  token = Token.decode_token(jwt_token.credentials)

  # validate access token against 
  canvas_user = token.validate_self()

  user = User.get_user_by_canvas_id(canvas_user['id'], db)

  if not User:
    return redir_to_oauth()

  return user


async def get_current_active_user(
  current_user: User = Depends(get_current_user)
):    
  """
  Gets current active user thats making an api request

  returns the User mapped class 
  raises unauthenticated exception if the user is disabled in the database
  """
  if current_user.disabled:
    raise HTTPException(status_code=400, detail="Inactive User")
  return current_user
