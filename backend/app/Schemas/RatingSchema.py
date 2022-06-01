from pydantic import BaseModel, constr
from datetime import datetime


class Rating(BaseModel):
    title: constr(max_length=255)
    short_description: constr(max_length=255)
    description: constr(max_length=1000)


class CreateRating(Rating):
    pass


class RatingInDB(Rating):
    id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True
