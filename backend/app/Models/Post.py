from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from .User import Base


class Post(Base):

    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, index=True)
    description: str = Column(String(length=1000), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')

    def __init__(self, title, description, user) -> None:
        self.title = title
        self.description = description
        self.user = user
        super().__init__()

    def save_self(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self







