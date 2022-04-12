from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class RatingModel(Base):
    """
    Mapped Aspect class

    Represents an aspect in the database
    """
    __tablename__ = 'rating'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String(length=255), nullable=False, index=True)
    short_description: str = Column(String(length=255), nullable=False)
    description: str = Column(String(length=1000), nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now())

    def __init__(self, title: str, short_description: str, description: str,) -> None:
        self.title = title
        self.short_description = short_description
        self.description = description
        super().__init__()
