from pydantic import BaseModel
from datetime import datetime


class AspectRating(BaseModel):
    title: str
    short_description: str
    description: str


class CreateAspectRating(AspectRating):
    pass


class AspectRatingInDB(AspectRating):
    id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True
