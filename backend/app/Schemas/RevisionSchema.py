from datetime import datetime
from pydantic import BaseModel, constr
from .FileSchema import CreateFile


class Revision(BaseModel):
    description: constr(max_length=1000)


class RevisionInDB(Revision):
    id: int
    post_id: int
    time_created: datetime

    class Config:
        orm_mode = True


class CreateRevision(Revision):
    file: CreateFile
