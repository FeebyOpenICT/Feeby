from Schemas.UserSchema import UserPublicSearch
from typing import List
from pydantic import BaseModel
from datetime import datetime


class Post(BaseModel):
    title: str
    description: str


class CreatePost(Post):
    pass


class PostInDB(Post):
    id: int
    user_id: int
    time_created: datetime
    time_updated: datetime
    users_with_access: List[UserPublicSearch]

    class Config:
        orm_mode = True
