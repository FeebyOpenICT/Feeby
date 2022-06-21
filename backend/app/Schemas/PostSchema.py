from datetime import datetime
from typing import List

from pydantic import BaseModel, constr

from Schemas.RevisionSchema import CreateInitialRevision, RevisionInDB


class Post(BaseModel):
    title: constr(max_length=255)
    description: constr(max_length=1000)


class CreatePost(Post):
    revision: CreateInitialRevision


class PostInDB(Post):
    id: int
    user_id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True


class PostInDBFull(PostInDB):
    revisions: List[RevisionInDB]


class PostInDBPublic(BaseModel):
    id: int
    user_id: int

    class Config:
        orm_mode = True
