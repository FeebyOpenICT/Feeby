
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
    access_to_posts: "List[PostInDB]"

    class Config:
        orm_mode = True


class UserPublicSearch(BaseModel):
    fullname: str
    canvas_email: str
    id: int

    class Config:
        orm_mode = True


# needs to be at the bottom don't move
from Schemas.PostSchema import PostInDB
UserInDB.update_forward_refs()
