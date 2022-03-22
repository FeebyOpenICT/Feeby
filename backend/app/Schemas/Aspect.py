from pydantic import BaseModel
from datetime import datetime


class Aspect(BaseModel):
    title: str
    short_description: str
    description: str
    external_url: str


class CreateAspect(Aspect):
    pass


class AspectInDB(Aspect):
    id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True
