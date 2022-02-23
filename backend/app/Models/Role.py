from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base

class Role(Base):
  __tablename__ = 'role'

  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String(length=255), nullable=False)
  description = Column(String(length=1000), nullable=False)

  def __repr__(self) -> str:
    return f"<Role title={self.title} description={self.description}>"
