from typing import List
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Session

from Models.SaveableModel import SaveableModel
from .RoleModel import RoleModel
from database import Base


class UserModel(Base, SaveableModel):
    """
    Mapped User class

    Represents a user in the database
    """
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(String(length=255), nullable=False, index=True)
    canvas_email = Column(String(length=255), nullable=False, unique=True)
    canvas_id = Column(Integer, nullable=False, unique=True, index=True)
    disabled = Column(Boolean, nullable=False, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    roles = relationship("RoleModel", secondary='user_role')

    def __init__(
        self,
        fullname: str,
        canvas_email: str,
        canvas_id: int,
        disabled: bool,
        roles: List[RoleModel],
        **kwargs
    ) -> None:
        self.fullname = fullname
        self.canvas_email = canvas_email
        self.canvas_id = canvas_id
        self.disabled = disabled
        if len(roles) == 0:
            raise ValueError("roles may not be empty")
        self.roles = roles
        self.access_to_posts = []
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<User id={self.id} canvas_email={self.canvas_email} roles={self.roles} fullname={self.fullname} canvas_id={self.canvas_id} disabled={self.disabled}>"
