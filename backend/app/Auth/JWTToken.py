from typing import List
from jose import jwt
from fastapi import status, HTTPException
import requests

from config import JWT_ALGORITHM, JWT_SECRET, BASE_URL
from Models.Role import Roles

class AccessToken:
  """
  JWT Token class for encoding, decoding and validating

  Not in database but can decode, encode and validate itself against canvas
  """
  def __init__(self, canvas_id: int, fullname: str, email: str, roles: List[dict], access_token: str = None, refresh_token: str = None) -> None:
    self.access_token = access_token
    self.refresh_token = refresh_token
    self.canvas_id = canvas_id
    self.fullname = fullname
    self.email = email
    self.roles = roles

  def __repr__(self) -> str:
    return f"canvas_id={self.canvas_id} access_token={self.access_token} refresh_token={self.refresh_token} scopes={self.roles}>"

  @property
  def encoded_token(self):
    """
    encoded jwt token
    """
    return jwt.encode({
      "access_token": self.access_token,
      "refresh_token": self.refresh_token,
      "canvas_id": self.canvas_id,
      "email": self.email,
      "fullname": self.fullname,
      "roles": self.roles
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

    if self.canvas_id != json['id']:
      raise HTTPException(403, "Invalid user_id, please reauthenticate", {"WWW-Authenticate": "Bearer"})

    return json

  
  def format_roles(canvas_ext_roles):
    """
    Formats the canvas roles to internal tool roles

    returns a list of strings of all roles that apply
    """

    """
    Admin
    "roles": [
        "urn:lti:instrole:ims/lis/Administrator",
        "urn:lti:instrole:ims/lis/Instructor",
        "urn:lti:role:ims/lis/Instructor",
        "urn:lti:sysrole:ims/lis/SysAdmin",
        "urn:lti:sysrole:ims/lis/User"
    ]

    Content designer
    "roles": [
        "urn:lti:instrole:ims/lis/Instructor",
        "urn:lti:role:ims/lis/ContentDeveloper",
        "urn:lti:sysrole:ims/lis/User"
    ]

    TA
    "roles": [
        "urn:lti:role:ims/lis/TeachingAssistant",
        "urn:lti:sysrole:ims/lis/User"
    ]

    Teacher
    "roles": [
        "urn:lti:instrole:ims/lis/Instructor",
        "urn:lti:role:ims/lis/Instructor",
        "urn:lti:sysrole:ims/lis/User"
    ]

    Observer
    "roles": [
        "urn:lti:role:ims/lis/Learner/NonCreditLearner",
        "urn:lti:role:ims/lis/Mentor",
        "urn:lti:sysrole:ims/lis/User"
    ]

    Student
    "roles": [
        "urn:lti:instrole:ims/lis/Student",
        "urn:lti:role:ims/lis/Learner",
        "urn:lti:sysrole:ims/lis/User"
    ]
    """
    roles: List[str] = []

    if "urn:lti:instrole:ims/lis/Administrator" in canvas_ext_roles or "urn:lti:sysrole:ims/lis/SysAdmin" in canvas_ext_roles:
      roles.append(Roles.ADMIN['title'])
    if "urn:lti:instrole:ims/lis/Instructor" in canvas_ext_roles or "urn:lti:role:ims/lis/Instructor" in canvas_ext_roles:
      roles.append(Roles.INSTRUCTOR['title'])
    if "urn:lti:role:ims/lis/ContentDeveloper" in canvas_ext_roles:
      roles.append(Roles.CONTENT_DEVELOPER['title'])
    if "urn:lti:role:ims/lis/TeachingAssistant" in canvas_ext_roles:
      roles.append(Roles.TEACHING_ASSISTANT['title'])
    if "urn:lti:instrole:ims/lis/Student" in canvas_ext_roles or "urn:lti:role:ims/lis/Learner" in canvas_ext_roles:
      roles.append(Roles.STUDENT['title'])
    if "urn:lti:role:ims/lis/Learner/NonCreditLearner" in canvas_ext_roles or "urn:lti:role:ims/lis/Mentor" in canvas_ext_roles:
      roles.append(Roles.OBSERVER['title'])
    
    return roles


  def decode_token(token: str):
    """
    Decodes the token

    Returns a Token class
    """
    try:
      payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

      canvas_id: int = payload.get("canvas_id")
      access_token: str = payload.get("access_token")
      refresh_token: str = payload.get("refresh_token")
      fullname: str = payload.get("fullname")
      email: str = payload.get("email")

      if canvas_id is None:
        raise HTTPException(403, "Invalid user_id, please reauthenticate", {"WWW-Authenticate": "Bearer"})

      roles = payload.get("roles", [])
    except (jwt.JWTError):
      raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Could not validate JWT token", {"WWW-Authenticate": "Bearer"})
    
    return AccessToken(
      roles=roles, 
      canvas_id=canvas_id,
      fullname=fullname,
      access_token=access_token,
      refresh_token=refresh_token,
      email=email,
    )
