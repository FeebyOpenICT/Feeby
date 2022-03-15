
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from Schemas.Role import GetRole


class GetUser(BaseModel):
  id: int
  fullname: str
  canvas_email: str
  canvas_id: int
  disabled: bool
  time_created: datetime
  time_updated: Optional[datetime]

  role: GetRole

  class Config:
    orm_mode = True
    # schema_extra = {
    #   "example": {
    #     "id": 1,
    #     "fullname": "Alex Duncan",
    #     "canvas_email": "alex.duncan@fake.domain.com",
    #     "canvas_id": 12,
    #     "disabled": False,

    #     "time_created": how to do this?,
    #     "time_updated": how to do this?,

        
    #     "role": GetRole
    #   }
    # }
