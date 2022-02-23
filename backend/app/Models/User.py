from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from .Role import Base

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, nullable=False)
  fullname = Column(String(length=255), nullable=False)
  canvas_email = Column(String(length=255), nullable=False, unique=True)
  canvas_id = Column(Integer, nullable=False, unique=True)
  access_token = Column(String, nullable=True)
  refresh_token = Column(String, nullable=True)
  expires_at = Column(Date, nullable=True)

  role_id = Column(Integer, ForeignKey('role.id'))
  role = relationship('Role')

  def __repr__(self) -> str:
    return f"<User id={self.id} email={self.email} role={self.role} fullname={self.fullname} canvas_id={self.canvas_id}>"
