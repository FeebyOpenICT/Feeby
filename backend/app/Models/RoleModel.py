from sqlalchemy import Column, Integer, String

from .SaveableModel import SaveableModel
from database import Base


class RoleModel(Base, SaveableModel):
    """
    Mapped Role class

    Represents a role in the database
    """
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False,
                        unique=True, index=True)

    def __init__(self, title: str) -> None:
        self.title = title
        super().__init__()

    def __repr__(self) -> str:
        return f"<Role title={self.title}>"
