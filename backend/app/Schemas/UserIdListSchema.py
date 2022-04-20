from typing import List
from pydantic import BaseModel


class UserIdList(BaseModel):
    user_ids: List[int]
