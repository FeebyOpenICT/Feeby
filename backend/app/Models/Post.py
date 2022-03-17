from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Session, relationship
from .User import Base


class Post(Base):
    """
    Mapped Post class

    Represents a post in the database
    """
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, index=True)
    description: str = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')

    def __init__(self, title, description, user) -> None:
        self.title = title
        self.description = description
        self.user = user
        super().__init__()

    def get_posts_by_user_id(user_id: int, db: Session):
        """
        Gets post object mapping from db
        """
        db_posts = db.query(Post).filter(Post.user_id == user_id).all()
        return db_posts

    def save_self(self, db: Session):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self
