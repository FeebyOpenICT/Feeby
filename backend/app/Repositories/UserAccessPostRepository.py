from typing import List, Optional
from Models.UserAccessPostModel import UserAccessPostModel
from sqlalchemy.orm import Session
from Exceptions import UnexpectedInstanceError


class UserAccessPostRepository:
    @staticmethod
    def get_by_id(post_id: int, user_id: int, db: Session) -> Optional[UserAccessPostModel]:
        """get User Access Post by id

        Args:
            post_id (int): id of post
            user_id (int): id of user
            db (Session): database session

        Returns:
            Optional[UserAccessPostModel]: returns UserAccessPostModel if user has access to post
        """
        result = db.query(UserAccessPostModel).filter(
            UserAccessPostModel.post_id == post_id, UserAccessPostModel.user_id == user_id).first()
        return result

    @staticmethod
    def save(user_access_post_model: UserAccessPostModel, db: Session) -> UserAccessPostModel:
        """save user access post model

        Args:
            user_access_post_model (UserAccessPostModel): user accesspost model
            db (Session): database session

        Raises:
            UnexpectedInstance: if instance is not of UserAccessPostModel

        Returns:
            UserAccessPostModel: UserAccessPostModel as saved in database
        """
        if not isinstance(user_access_post_model, UserAccessPostModel):
            raise UnexpectedInstanceError

        db.add(user_access_post_model)
        db.flush()
        db.refresh(user_access_post_model)

        return user_access_post_model
