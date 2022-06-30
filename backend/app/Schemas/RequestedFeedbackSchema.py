from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, conlist

from .UserSchema import UserPublicInDB


class RequestedFeedbackBase(BaseModel):
    pass


class CreateRequestedFeedback(RequestedFeedbackBase):
    users: conlist(UserPublicInDB, min_items=1)


class RequestedFeedbackInDB(RequestedFeedbackBase):
    uuid: UUID4
    time_created: datetime
    time_opened: Optional[datetime]
    time_finished: Optional[datetime]

    user: UserPublicInDB

    class Config:
        orm_mode = True
