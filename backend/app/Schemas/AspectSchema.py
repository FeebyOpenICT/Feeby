from typing import List, Optional
from pydantic import BaseModel, constr, validator
from datetime import datetime
from .RatingSchema import RatingInDB


class Aspect(BaseModel):
    title: constr(max_length=255)
    short_description: constr(max_length=255)
    description: constr(max_length=1000)
    external_url: constr(max_length=2000)


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


class UpdateAspect(BaseModel):
    title: Optional[constr(max_length=255)] = None
    short_description: Optional[constr(max_length=255)] = None
    description: Optional[constr(max_length=1000)] = None
    external_url: Optional[constr(max_length=2000)] = None
    rating_ids: Optional[List[int]] = None

    @validator('rating_ids', pre=True, always=True)
    def validate_ids_length(cls, value):
        if isinstance(value, List):
            if len(value) == 0:
                raise ValueError("empty rating not allowed")
        return value
