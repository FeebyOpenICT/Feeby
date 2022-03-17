from typing import List
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Session

from .Role import Role, Roles
from .User_Role import Base
from Exceptions.NotFound import NotFound

class User(Base):
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
  time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

  roles = relationship("Role", secondary='user_role')

  def __init__(
    self, 
    fullname: str = None, 
    canvas_email: str = None, 
    canvas_id: int = None, 
    disabled: bool = False,
    roles: List[Role] = [],
    **kwargs
  ) -> None:
    self.fullname = fullname
    self.canvas_email = canvas_email
    self.canvas_id = canvas_id
    self.disabled = disabled
    self.roles = roles
    super().__init__(**kwargs)


  def __repr__(self) -> str:
    return f"<User id={self.id} canvas_email={self.canvas_email} role={self.role} fullname={self.fullname} canvas_id={self.canvas_id} disabled={self.disabled}>"


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

  
  def get_user_by_id(id: int, db: Session):
    """
    Gets the user by their id

    id = integer equal to the the id

    Returns a python user mapped class from the database
    """
    user = db.query(User).filter(User.id == id).first()

    if not User:
      raise NotFound("user")

    return user


  def save_self(self, db: Session):
    """
    Saves own instance in the database

    Returns a python user mapped class from the database
    """
    db.add(self)
    db.commit()
    db.refresh(self)
    return self
