from dataclasses import dataclass
import sqlite3
from typing import List
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Session

from Models.SaveableModel import SaveableModel
from .Role import Role
from .User_Role import Base

from Exceptions.NotFound import NotFound


class User(Base, SaveableModel):
    """
    Mapped User class

    Represents a user in the database
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    fullname = Column(String(length=255), nullable=False, index=True)
    canvas_email = Column(String(length=255), nullable=False, unique=True)
    canvas_id = Column(Integer, nullable=False, unique=True, index=True)
    disabled = Column(Boolean, nullable=False, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    roles = relationship("Role", secondary='user_role')

    def __init__(
        self,
        fullname: str,
        canvas_email: str,
        canvas_id: int,
        disabled: bool,
        roles: List[Role],
        **kwargs
    ) -> None:
        self.fullname = fullname
        self.canvas_email = canvas_email
        self.canvas_id = canvas_id
        self.disabled = disabled
        if len(roles) == 0:
            raise ValueError("roles may not be empty")
        self.roles = roles
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<User id={self.id} canvas_email={self.canvas_email} roles={self.roles} fullname={self.fullname} canvas_id={self.canvas_id} disabled={self.disabled}>"

    # static not class method because I want it to always return a User instance
    @staticmethod
    def get_user_by_canvas_id(id: int, db: Session):
        """
        Gets the user by their canvas id

        id = integer equal to the the canvas id

        Returns a python user mapped class from the database
        """
        user = db.query(User).filter(User.canvas_id == id).first()

        if not user:
            raise NotFound("user")

        return user

    # static not class method because I want it to always return a User instance
    @staticmethod
    def get_user_by_id(id: int, db: Session):
        """
        Gets the user by their id

        id = integer equal to the the id

        Returns a python user mapped class from the database
        """
        user = db.query(User).filter(User.id == id).first()

        if not User:
            raise NotFound(f"user: {id}")

        return user
