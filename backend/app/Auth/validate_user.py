from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
    OAuth2PasswordBearer,
    SecurityScopes,
    OAuth2AuthorizationCodeBearer
)

from .redir_to_auth import redir_to_oauth


from .JWTToken import AccessToken
from Models.User import User
from Models.Role import Roles
from database import get_db_connection

# automatically checks if there is a Bearer ... token in the Authorizaiton header
token_auth_scheme = OAuth2PasswordBearer(
  "jwt",
  scopes={
    Roles.ADMIN['title']: Roles.ADMIN['description'],
    Roles.STUDENT['title']: Roles.STUDENT['description'],
    Roles.OBSERVER['title']: Roles.OBSERVER['description'],
    Roles.CONTENT_DEVELOPER['title']: Roles.CONTENT_DEVELOPER['description'],
    Roles.INSTRUCTOR['title']: Roles.INSTRUCTOR['description'],
    Roles.TEACHING_ASSISTANT['title']: Roles.TEACHING_ASSISTANT['description'],
  }
)


async def get_current_user(
  security_scopes: SecurityScopes,
  jwt_token: HTTPAuthorizationCredentials = Depends(token_auth_scheme), 
  db: Session = Depends(get_db_connection),
) -> User:
  """
  Gets the current user from the database by decoding the jwt bearer token

  Also checks allowed roles

  Returns the User mapped class
  """
  if security_scopes.scopes:
    required_roles = security_scopes.scopes

  token = AccessToken.decode_token(jwt_token)

  if required_roles and not token.roles:
    # no roles in token, something went wrong whilst making the token.
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No roles found in jwt token")
  
  has_required_role = False

  for token_role in token.roles:
    if token_role in required_roles:
      has_required_role = True

  if has_required_role == False:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")

  # validate access token against 
  canvas_user = token.validate_self()

  user = User.get_user_by_canvas_id(canvas_user['id'], db)

  if not User:
    return redir_to_oauth()

  return user


async def get_current_active_user(
  current_user: User = Security(get_current_user, scopes=[])
) -> User:    
  """
  Gets current active user thats making an api request

  returns the User mapped class 
  raises unauthenticated exception if the user is disabled in the database
  """
  if current_user.disabled:
    raise HTTPException(status_code=400, detail="Inactive User")
  return current_user
