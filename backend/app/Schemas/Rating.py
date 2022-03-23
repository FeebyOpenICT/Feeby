from pydantic import BaseModel
from datetime import datetime


class Rating(BaseModel):
    title: str
    short_description: str
    description: str


class CreateRating(Rating):
    pass


class RatingInDB(Rating):
    id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True
