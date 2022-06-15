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
    revision_id: Optional[int]
    feedback_id: Optional[int]
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True


class CreateFile(BaseModel):
    revision_id: Optional[int]
    feedback_id: Optional[int]
