from typing import List
from Models.PostModel import PostModel
from Models.UserAccessPostModel import UserAccessPostModel
from Models.UserModel import UserModel
from sqlalchemy.orm import Session


class UserAccessPostRepository:
    @staticmethod
    def grant_access_to_users_to_post(post: PostModel, users: List[UserModel], db: Session) -> List[UserAccessPostModel]:
        accessList = []

        for user in users:
            access = UserAccessPostModel(post=post, user=user)
            accessList.append(access)

        db.add_all(accessList)
        db.commit()

        return accessList
