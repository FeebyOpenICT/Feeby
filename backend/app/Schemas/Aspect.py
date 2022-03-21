from pydantic import BaseModel
from datetime import datetime


class CreateAspect(BaseModel):
    title: str
    short_description: str
    description: str
    external_url: str


class AspectInDB(CreateAspect):
    id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True

