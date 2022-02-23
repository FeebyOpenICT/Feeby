from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

from .Role import Base

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  fullname = Column(String(length=255))
  email = Column(String(length=255), unique=True)
  canvas_id = Column(Integer, unique=True)
  access_token = Column(String)

  role_id = Column(Integer, ForeignKey('role.id'))
  role = relationship('Role')

  def __repr__(self) -> str:
    return f"<User id={self.id} email={self.email} role={self.role} fullname={self.fullname} canvas_id={self.canvas_id}>"
