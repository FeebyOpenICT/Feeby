from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base

class Role(Base):
  __tablename__ = 'role'

  id = Column(Integer, primary_key=True)
  title = Column(String(length=255))
  description = Column(String(length=1000))

  def __repr__(self) -> str:
    return f"<Role title={self.title} description={self.description}>"
