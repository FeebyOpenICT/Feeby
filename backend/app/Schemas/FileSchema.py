from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional
from Models import RevisionModel, FeedbackModel


class File(BaseModel):
    filename: constr(max_length=255)
    content_type: constr(max_length=255)
    location: constr(max_length=255)


class FileInDB(File):
    id: int
    revision_id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True


class CreateFile(File):
    revision_id: Optional[RevisionModel]
    feedback_id: Optional[FeedbackModel]
