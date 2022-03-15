from pydantic import BaseModel
from datetime import datetime


class CreatePost(BaseModel):
    title: str
    description: str


class PostInDB(CreatePost):
    id: int
    user_id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True

