from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PostBody(BaseModel):
  title: str
  description: str
  time_created: datetime
  time_updated: Optional[datetime]
