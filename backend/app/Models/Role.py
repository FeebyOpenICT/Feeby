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
    return admin_role
  
  def get_teacher_role(db: Session):
    """
    Gets the teacher role object mapping

    db = db connection session
    """
    teacher_role = db.query(Role).filter(Role.title == 'teacher').first()
    if not teacher_role:
      # no student role in db, create one
      teacher_role = Role(title="teacher", description="I am a teacher")
      db.add(teacher_role)
      db.commit()
    return teacher_role