from pydantic import BaseModel


class IdsInDBSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True
