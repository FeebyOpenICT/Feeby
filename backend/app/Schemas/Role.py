from pydantic import BaseModel


class Role(BaseModel):
    title: str
    description: str


class RoleInDB(Role):
    id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "description": "I am an admin, I have permissions to edit everything and see everything within the tool.",
                "title": "admin",
            }
        }
