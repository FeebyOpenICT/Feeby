from typing import List
from jose import jwt
from fastapi import status, HTTPException
import requests

from config import JWT_ALGORITHM, JWT_SECRET, BASE_URL


class RolesToken:
  """
  JWT Token class for encoding and decoing the roles passed to the tool at lti launch
  """
  def __init__(self, roles) -> None:
    # TODO decode canvas roles to simpler understood roles
    """
    All roles ive found so far:

    urn:lti:instrole:ims/lis/Administrator,
    urn:lti:instrole:ims/lis/Instructor,
    urn:lti:role:ims/lis/Instructor,
    urn:lti:sysrole:ims/lis/SysAdmin,
    urn:lti:sysrole:ims/lis/User
    urn:lti:instrole:ims/lis/Student,
    urn:lti:role:ims/lis/Learner,
    urn:lti:sysrole:ims/lis/User
    """
    self.roles = roles

  @property
  def encoded_token(self):
    """
    encoded jwt token
    """
    return jwt.encode({
      "roles": self.roles
    }, JWT_SECRET, algorithm=JWT_ALGORITHM)
  
  # def get_roles_from_token(self, token):
  #   """
  #   Gets the roles from an encoded token

  #   returns a list of strings including all roles
  #   """
  #   jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

class AccessToken:
  """
  JWT Token class for encoding, decoding and validating

  Not in database but can decode, encode and validate itself against canvas
  """
  def __init__(self, access_token: str, refresh_token: str, canvas_id: int, scopes: List[str]) -> None:
    self.access_token = access_token
    self.refresh_token = refresh_token
    self.canvas_id = canvas_id
    self.scopes = scopes

  def __repr__(self) -> str:
    return f"canvas_id={self.canvas_id} access_token={self.access_token} refresh_token={self.refresh_token} scopes={self.scopes}>"

  @property
  def encoded_token(self):
    """
    encoded jwt token
    """
    return jwt.encode({
      "access_token": self.access_token,
      "refresh_token": self.refresh_token,
      "canvas_id": self.canvas_id,
      "scopes": self.scopes
    }, JWT_SECRET, algorithm=JWT_ALGORITHM)


  def validate_self(self):
    """
    validates the token against the canvas api

    returns canvas self from /api/v1/users/self
    """
    headers = {
      "Authorization": f"Bearer {self.access_token}"
    }
    r = requests.get(f'{BASE_URL}/api/v1/users/self', headers=headers)
    
    if r.status_code >= 400: 
      # Something went wrong on canvas's side, forward error to frontend
      raise HTTPException(status_code=r.status_code, detail=r.json())

    json = r.json()
    return json


  def decode_token(token: str):
    """
    Decodes the token

    Returns a Token class
    """
    credentials_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Could not validate jwt token",
      headers={"WWW-Authenticate": "Bearer"},
    )

    try:
      payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

      canvas_id: int = payload.get("canvas_id")
      access_token: str = payload.get("access_token")
      refresh_token: str = payload.get("refresh_token")

      if canvas_id is None or access_token is None:
        raise credentials_exception

      token_scopes = payload.get("scopes", [])
    except (jwt.JWTError):
      raise credentials_exception
    
    return AccessToken(
      scopes=token_scopes, 
      canvas_id=canvas_id,
      access_token=access_token,
      refresh_token=refresh_token
    )