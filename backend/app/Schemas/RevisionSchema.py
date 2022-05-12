from datetime import datetime
from typing import List
from pydantic import BaseModel, constr
from Schemas.FeedbackSchema import CreateFeedback


class Revision(BaseModel):
    description: constr(max_length=1000)


class RevisionInDB(Revision):
    id: int
    post_id: int
    time_created: datetime

    class Config:
        orm_mode = True


class CreateInitialRevision(Revision):
    feedback: List[CreateFeedback]


class CreateRevision(Revision):
    pass
