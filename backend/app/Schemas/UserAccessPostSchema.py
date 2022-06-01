from datetime import datetime
from pydantic import BaseModel


class UserAccessPost(BaseModel):
    post_id: int
    user_id: int


class UserAccessPostInDB(UserAccessPost):
    time_created: datetime

    class Config:
        orm_mode = True
