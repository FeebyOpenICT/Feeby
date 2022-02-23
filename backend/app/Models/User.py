from datetime import date
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .Role import Base

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, nullable=False)
  fullname = Column(String(length=255), nullable=False)
  canvas_email = Column(String(length=255), nullable=False, unique=True)
  canvas_id = Column(Integer, nullable=False, unique=True, index=True)
  access_token = Column(String, nullable=True)
  refresh_token = Column(String, nullable=True)
  expires_at = Column(Date, nullable=True)

  role_id = Column(Integer, ForeignKey('role.id'))
  role = relationship('Role')

  def __init__(
    self, 
    fullname: str, 
    canvas_email: str, 
    canvas_id: int, 
    access_token: str = None, 
    refresh_token: str = None,
    expires_at: date = None,
    **kwargs
  ) -> None:
    self.fullname = fullname
    self.canvas_email = canvas_email
    self.canvas_id = canvas_id
    self.access_token = access_token
    self.refresh_token = refresh_token
    self.expires_at = expires_at
    super().__init__(**kwargs)

  def __repr__(self) -> str:
    return f"<User id={self.id} canvas_email={self.canvas_email} role={self.role} fullname={self.fullname} canvas_id={self.canvas_id}>"
