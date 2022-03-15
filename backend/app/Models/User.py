from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Session
from fastapi import HTTPException
from .Role import Base, Role
from Exceptions.NotFound import NotFound
class User(Base):
  """
  Mapped User class

  Represents a user in the database
  """
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True, nullable=False)
  fullname = Column(String(length=255), nullable=False, index=True)
  canvas_email = Column(String(length=255), nullable=False, unique=True)
  canvas_id = Column(Integer, nullable=False, unique=True, index=True)
  disabled = Column(Boolean, nullable=False, default=False)
  time_created = Column(DateTime(timezone=True), server_default=func.now())
  time_updated = Column(DateTime(timezone=True), onupdate=func.now())

  role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
  role: Role = relationship('Role')

  def __init__(
    self, 
    fullname: str = None, 
    canvas_email: str = None, 
    canvas_id: int = None, 
    disabled: bool = False,
    **kwargs
  ) -> None:
    self.fullname = fullname
    self.canvas_email = canvas_email
    self.canvas_id = canvas_id
    self.disabled = disabled
    super().__init__(**kwargs)

  def __repr__(self) -> str:
    return f"<User id={self.id} canvas_email={self.canvas_email} role={self.role} fullname={self.fullname} canvas_id={self.canvas_id} disabled={self.disabled}>"

  def get_user_by_canvas_id(id: int, db: Session):
    """
    Gets the user by their canvas id

    id = integer equal to the the canvas id

    Returns a python user mapped class from the database
    """
    result = db.query(User, Role).filter(User.canvas_id == id).join(User.role).first()

    if not result:
      raise NotFound("user")

    user, role = result
    user.role = role
    return user


  def save_self(self, db: Session):
    """
    Saves own instance in the database

    Returns a python user mapped class from the database
    """
    db.add(self)
    db.commit()
    db.refresh(self)
    return self


class Student(User):
  """
  User class with student role auto assigned
  """
  def __init__(self, db: Session, fullname: str = None, canvas_email: str = None, canvas_id: int = None, **kwargs) -> None:
    self.role = Role.get_student_role(db)
    super().__init__(fullname, canvas_email, canvas_id, **kwargs)


class Instructor(User):
  """
  User class with instructor role auto assigned
  """
  def __init__(self, db: Session, fullname: str = None, canvas_email: str = None, canvas_id: int = None, **kwargs) -> None:
    self.role = Role.get_instructor_role(db)
    super().__init__(fullname, canvas_email, canvas_id, **kwargs)


class Observer(User):
  """
  User class with observer role auto assigned
  """
  def __init__(self, db: Session, fullname: str = None, canvas_email: str = None, canvas_id: int = None, **kwargs) -> None:
    self.role = Role.get_observer_role(db)
    super().__init__(fullname, canvas_email, canvas_id, **kwargs)


class Admin(User):
  """
  User class with admin role auto assigned
  """
  def __init__(self, db: Session, fullname: str = None, canvas_email: str = None, canvas_id: int = None, **kwargs) -> None:
    self.role = Role.get_admin_role(db)
    super().__init__(fullname, canvas_email, canvas_id, **kwargs)



class ContentDeveloper(User):
  """
  User class with content developer role auto assigned
  """
  def __init__(self, db: Session, fullname: str = None, canvas_email: str = None, canvas_id: int = None, **kwargs) -> None:
    self.role = Role.get_content_developer_role(db)
    super().__init__(fullname, canvas_email, canvas_id, **kwargs)


class TeachingAssistant(User):
  """
  User class with teaching assistant role auto assigned
  """
  def __init__(self, db: Session, fullname: str = None, canvas_email: str = None, canvas_id: int = None, **kwargs) -> None:
    self.role = Role.get_teaching_assistant_role(db)
    super().__init__(fullname, canvas_email, canvas_id, **kwargs)
