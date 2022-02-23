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
