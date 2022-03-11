from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from .User import Base


class Post(Base):

    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, unique=True, index=True)
    description: str = Column(String(length=1000), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    role = relationship('User')

    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description
        super().__init__()

    def save_self(self, db: Session):
        """
        Saves own instance in the database

        Returns a python user mapped class from the database
        """
        db.add(self)
        db.commit()
        db.refresh(self)
        return self






