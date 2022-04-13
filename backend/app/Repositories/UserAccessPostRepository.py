from typing import List
from Models.PostModel import PostModel
from Models.UserAccessPostModel import UserAccessPostModel
from Models.UserModel import UserModel
from sqlalchemy.orm import Session


class UserAccessPostRepository:
    @staticmethod
    def grant_access_to_users_to_post(post: PostModel, users: List[UserModel], db: Session) -> List[UserAccessPostModel]:
        """Grant access to users on post

        Args:
            post (PostModel): post to grant access to
            users (List[UserModel]): list of users to grant access to post
            db (Session): database session

        Returns:
            List[UserAccessPostModel]: list of users that now have access to the post
        """
        accessList = []

        for user in users:
            access = UserAccessPostModel(post=post, user=user)
            accessList.append(access)

        db.add_all(accessList)
        db.commit()

        return accessList
