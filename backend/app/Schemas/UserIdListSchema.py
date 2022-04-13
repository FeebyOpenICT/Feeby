from typing import List
from pydantic import BaseModel, validator


class UserIdList(BaseModel):
    user_ids: List[int]

    @validator('user_ids', pre=True, always=True)
    def validate_ids_length(cls, value):
        if len(value) == 0:
            raise ValueError("empty list not allowed")
        return value
