
from datetime import datetime
from typing import List
from pydantic import BaseModel
from Schemas.Role import RoleInDB


class User(BaseModel):
  fullname: str
  canvas_email: str
  canvas_id: int
  disabled: bool
  roles: List[RoleInDB]


class UserInDB(User):
  id: int
  time_created: datetime
  time_updated: datetime
  class Config:
    orm_mode = True
