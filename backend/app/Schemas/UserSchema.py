
from datetime import datetime
from typing import List
from pydantic import BaseModel, constr
from Schemas.RoleSchema import RoleInDB


class UserPublic(BaseModel):
    fullname: constr(max_length=255)
    canvas_email: constr(max_length=255)


class User(UserPublic):
    canvas_id: int
    disabled: bool
    roles: List[RoleInDB]


class UserInDB(User):
    id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True


class UserPublicInDB(UserPublic):
    id: int

    class Config:
        orm_mode = True
