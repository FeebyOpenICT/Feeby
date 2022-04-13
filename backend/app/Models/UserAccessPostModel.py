from Models.PostModel import PostModel
from Models.UserModel import UserModel
from database import Base
from sqlalchemy import Column, ForeignKey, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class UserAccessPostModel(Base):
    """UserAccessPostModel
    """
    __tablename__ = 'user_access_post'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship("UserModel", backref="user_access_post")

    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    post = relationship("PostModel", backref="user_access_post")

    time_created = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, user: UserModel, post: PostModel) -> None:
        """UserAccessPostModel constructor

        Args:
            user (UserModel): user that has access to the post
            post (PostModel): post the user will have access to
        """
        self.user = user
        self.post = post
