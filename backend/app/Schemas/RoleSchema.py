from pydantic import BaseModel


class Role(BaseModel):
    title: str


class RoleInDB(Role):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "admin",
            }
        }
