from typing import List

from fastapi import HTTPException, status
from Exceptions import DuplicateKey, NoPermissions

from Models import UserAccessPostModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Repositories import UserAccessPostRepository

from Services import PostService, UserService


class UserAccessPostService:
    @staticmethod
    def check_access_to_post_or_fail(post_id: int, user_id: int, db: Session):
        result = UserAccessPostRepository.get_by_id(
            post_id=post_id, user_id=user_id, db=db)

        if not result:
            raise NoPermissions(resource="post", id=post_id)

    @staticmethod
    def grant_access_to_post(post_id: int, user_id: int, user_ids: List[int], db: Session) -> List[UserAccessPostModel]:
        """grant access to post whilst checking for errors

        Args:
            post_id (int): post to grant access to
            user_id (int): id of the owner of the post
            user_ids (List[int]): list of user ids to give access to
            db (Session): database session

        Raises:
            HTTPException: if user_id is in user_ids
            NotFoundException: if post is not found
            NotFoundException: if any of the users in user_ids is not found
            DuplicateKey: if access has already been given to one of the users

        Returns:
            List[UserAccessPostModel]: list of access to user 
        """
        if user_id in user_ids:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Can't grant access to self")

        post = PostService.get_post_by_id_from_user_id_or_fail(
            post_id=post_id, user_id=user_id, db=db)

        users = [UserService.get_active_user_by_id_or_fail(
            id=id, db=db) for id in user_ids]

        try:
            accessList = [UserAccessPostRepository.save(user_access_post_model=UserAccessPostModel(
                user=user, post=post), db=db) for user in users]
        except IntegrityError as error:
            raise DuplicateKey(resource="User Access Post",
                               id=error.params['user_id'])

        return accessList
