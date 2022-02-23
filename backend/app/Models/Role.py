from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base

class Role(Base):
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
    student_role = db.query(Role).filter(Role.title == 'student').first()
    if not student_role:
      # no student role in db, create one
      student_role = Role(title="student", description="I am a student")
      db.add(student_role)
      db.commit()
      db.refresh(student_role)
    return student_role

  def get_external_expert_role(db: Session):
    """
    Gets the external_expert role object mapping

    db = db connection session
    """
    external_expert_role = db.query(Role).filter(Role.title == 'external_expert').first()
    if not external_expert_role:
      # no student role in db, create one
      external_expert_role = Role(title="external_expert", description="I am an external_expert")
      db.add(external_expert_role)
      db.commit()
      db.refresh(external_expert_role)
    return external_expert_role

  def get_admin_role(db: Session):
    """
    Gets the admin role object mapping

    db = db connection session
    """
    admin_role = db.query(Role).filter(Role.title == 'admin').first()
    if not admin_role:
      # no student role in db, create one
      admin_role = Role(title="admin", description="I am an admin")
      db.add(admin_role)
      db.commit()
      db.refresh(admin_role)
    return admin_role
  
  def get_instructor_role(db: Session):
    """
    Gets the instructor role object mapping

    db = db connection session
    """
    instructor_role = db.query(Role).filter(Role.title == 'instructor').first()
    if not instructor_role:
      # no student role in db, create one
      instructor_role = Role(title="instructor", description="I am a instructor")
      db.add(instructor_role)
      db.commit()
      db.refresh(instructor_role)
    return instructor_role
