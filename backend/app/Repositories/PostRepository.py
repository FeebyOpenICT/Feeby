from typing import List
from sqlalchemy.orm import Session

from Models.PostModel import PostModel


class PostRepository:
    """
    Repository class to do with posts
    """
    @staticmethod
    def get_posts_from_user_by_id(user_id: int, db: Session) -> List[PostModel]:
        """
        Gets all the posts from a user by their id

        user_id = integer equal to the the user id

        Returns a list of python Post mapped class from the database
        """
        result = db.query(PostModel).filter(PostModel.user_id == user_id).all()
        return result
