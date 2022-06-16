from datetime import datetime
from typing import List
from pydantic import BaseModel, constr
from typing import List, Optional
from Schemas.FeedbackSchema import CreateFeedback, Feedback, FeedbackInDB


class Revision(BaseModel):
    description: constr(max_length=1000)


class RevisionInDB(Revision):
    id: int
    post_id: int
    time_created: datetime

    class Config:
        orm_mode = True


class RevisionInDBFull(RevisionInDB):
    feedback: List[FeedbackInDB]


class CreateInitialRevision(Revision):
    feedback: List[CreateFeedback]


class CreateRevision(Revision):
    pass
