from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base

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

  # get_..._role are all seperate so that I can easily create them if they don't exist in the db yet
  def get_student_role(db: Session):
    """
    Gets the student role object mapping

    db = db connection session
    """
    role = db.query(Role).filter(Role.title == 'student').first()
    if not role:
      # no student role in db, create one
      role = Role(title="student", description="I am a student")
      db.add(role)
      db.commit()
      db.refresh(role)
    return role

  def get_observer_role(db: Session):
    """
    Gets the observer role object mapping

    db = db connection session
    """
    role = db.query(Role).filter(Role.title == 'observer').first()
    if not role:
      # no student role in db, create one
      role = Role(title="observer", description="I am an observer")
      db.add(role)
      db.commit()
      db.refresh(role)
    return role

  def get_admin_role(db: Session):
    """
    Gets the admin role object mapping

    db = db connection session
    """
    role = db.query(Role).filter(Role.title == 'admin').first()
    if not role:
      # no student role in db, create one
      role = Role(title="admin", description="I am an admin")
      db.add(role)
      db.commit()
      db.refresh(role)
    return role
  
  def get_instructor_role(db: Session):
    """
    Gets the instructor role object mapping

    db = db connection session
    """
    role = db.query(Role).filter(Role.title == 'instructor').first()
    if not role:
      # no student role in db, create one
      role = Role(title="instructor", description="I am a instructor")
      db.add(role)
      db.commit()
      db.refresh(role)
    return role

  def get_teaching_assisstent_role(db: Session):
    """
    Gets the teaching assisstent role object mapping

    db = db connection session
    """
    role = db.query(Role).filter(Role.title == 'teaching_assistant').first()
    if not role:
      # no student role in db, create one
      role = Role(title="teaching_assistant", description="I am a teaching_assistant")
      db.add(role)
      db.commit()
      db.refresh(role)
    return role

  def get_content_developer_role(db: Session):
    """
    Gets the content developer role object mapping

    db = db connection session
    """
    role = db.query(Role).filter(Role.title == 'content_developer').first()
    if not role:
      # no student role in db, create one
      role = Role(title="content_developer", description="I am a content developer")
      db.add(role)
      db.commit()
      db.refresh(role)
    return role
