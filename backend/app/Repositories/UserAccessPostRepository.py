from typing import List
from Models.UserAccessPostModel import UserAccessPostModel
from sqlalchemy.orm import Session
from Exceptions import UnexpectedInstanceError


class UserAccessPostRepository:
    @staticmethod
    def save(user_access_post_model: UserAccessPostModel, db: Session) -> UserAccessPostModel:
        """save user access post model

        Args:
            user_access_post_model (UserAccessPostModel): user accesspost model
            db (Session): database session

        Returns:
            UserAccessPostModel: UserAccessPostModel as saved in database
        """
        if not isinstance(user_access_post_model, UserAccessPostModel):
            raise UnexpectedInstanceError

        db.add(user_access_post_model)
        db.commit()

        return user_access_post_model
