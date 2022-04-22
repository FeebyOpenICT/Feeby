from pydantic import BaseModel, constr
from datetime import datetime


class File(BaseModel):
    location: constr(max_length=255)


class CreateFile(File):
    pass


class FileInDB(File):
    id: int
    post_id: int
    time_created: datetime
    time_updated: datetime

    class Config:
        orm_mode = True
