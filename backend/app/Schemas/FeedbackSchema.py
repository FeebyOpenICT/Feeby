from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr


class Feedback(BaseModel):
    description: constr(max_length=1000)


class CreateFeedback(Feedback):
    aspect_id: int
    rating_id: int


class FeedbackInDB(CreateFeedback):
    id: int
    time_created: datetime
    time_updated: datetime
