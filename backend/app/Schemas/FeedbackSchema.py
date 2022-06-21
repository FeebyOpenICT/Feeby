from datetime import datetime

from pydantic import BaseModel, constr

from Schemas import RatingInDB, AspectInDB


class Feedback(BaseModel):
    description: constr(max_length=1000)


class CreateFeedback(Feedback):
    aspect_id: int
    rating_id: int


class FeedbackInDB(Feedback):
    id: int
    time_created: datetime
    rating: RatingInDB
    aspect: AspectInDB

    class Config:
        orm_mode = True
