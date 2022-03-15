from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base

class Roles:
  """
  Constants for Roles in the tool
  """
  STUDENT = {
    "title": "student",
    "description": ""
  }

  OBSERVER = {
    "title": "observer",
    "description": ""
  }

  INSTRUCTOR = {
    "title": "instructor",
    "description": ""
  }

  ADMIN = {
    "title": "admin",
    "description": ""
  }

  TEACHING_ASSISTANT = {
    "title": "teaching_assistant",
    "description": ""
  }

  CONTENT_DEVELOPER = {
    "title": "content_developer",
    "description": ""
  }


class Role(Base):
  """
  Mapped Role class
  
  Represents a role in the database
  """
  __tablename__ = 'role'

  id = Column(Integer, primary_key=True, nullable=False)
  title: str = Column(String(length=255), nullable=False, unique=True, index=True)
  description: str = Column(String(length=1000), nullable=False)

  def __init__(self, title, description) -> None:
    self.title = title
    self.description = description
    super().__init__()

  def __repr__(self) -> str:
    return f"<Role title={self.title} description={self.description}>"

  def get_role(role, db: Session):
    """
    Gets role object mapping from db
    """
    role = db.query(Role).filter(Role.title == role.title).first()
    if not role:
      role = Role(title=role.title, description=role.description)
      db.add(role)
      db.commit()
      db.refresh(role)
    return role
