from typing import List
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .RoleModel import RoleModel
from database import Base


class UserModel(Base):
    """UserModel
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
        """UserModel constructor

        Args:
            fullname (str): fullname of the user
            canvas_email (str): canvas email of the user
            canvas_id (int): canvas id of the user
            disabled (bool): wether the user is still active within the system, for data warehousing purposes
            roles (List[RoleModel]): list of roles the user has, must have atleast one role

        Raises:
            ValueError: if roles is empty it will raise a valueerror
        """
        self.fullname = fullname
        self.canvas_email = canvas_email
        self.canvas_id = canvas_id
        self.disabled = disabled
        if len(roles) == 0:
            raise ValueError("roles may not be empty")
        self.roles = roles
        super().__init__(**kwargs)
