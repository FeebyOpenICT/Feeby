from datetime import datetime
from pydantic import BaseModel, constr
from typing import List, Optional
from .FormData import FormData


class Revision(BaseModel):
    description: constr(max_length=1000)


class RevisionInDB(Revision):
    id: int
    post_id: int
    time_created: datetime

    class Config:
        orm_mode = True


class CreateRevision(Revision):
    pass
