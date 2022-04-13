from pydantic import BaseModel, constr


class Role(BaseModel):
    title: constr(max_length=255)


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
