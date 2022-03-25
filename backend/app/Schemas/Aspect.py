from typing import List
from pydantic import BaseModel, validator
from datetime import datetime
from .Rating import RatingInDB


class Aspect(BaseModel):
    title: str
    short_description: str
    description: str
    external_url: str


class CreateAspect(Aspect):
    rating_ids: List[int]

    @validator('rating_ids', pre=True, always=True)
    def validate_ids_length(cls, value):
        if len(value) == 0:
            raise ValueError("empty list not allowed")
        return value


class AspectInDB(Aspect):
    id: int
    time_created: datetime
    time_updated: datetime
    ratings: List[RatingInDB]

    class Config:
        orm_mode = True