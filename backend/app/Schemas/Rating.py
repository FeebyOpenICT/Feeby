from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


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


class RatingUpdate(BaseModel):
    title: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
