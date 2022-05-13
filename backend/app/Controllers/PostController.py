from fastapi import Depends, status, HTTPException
from typing import List
from Schemas.UserAccessPostSchema import UserAccessPostInDB
from Services import UserAccessPostService
from Services.PostService import PostService
from Auth.validate_user import get_current_active_user, get_current_active_user_that_is_self
from sqlalchemy.orm import Session
from Schemas.PostSchema import CreatePost
from Schemas.UserIdListSchema import UserIdList
from database import get_db_connection
from Models.UserModel import UserModel
from Schemas.PostSchema import PostInDB
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from Services.UserService import UserService

router = InferringRouter(
    tags=["Posts"]
)


@cbv(router)
class PostController:
    user_id: int
    db: Session = Depends(get_db_connection)

    @router.get('/users/{user_id}/posts',  response_model=List[PostInDB])
    async def get_posts(self, current_active_user: UserModel = Depends(get_current_active_user)):
        """Get all posts from database

        Args:
            user_id (int): id of user in as saved in database

        Allowed roles:
        - All
        """
        result = PostService.get_posts_from_user_by_id_and_current_user_id(
            user_id=self.user_id, current_user_id=current_active_user.id, db=self.db)

        return result

    @router.post('/users/{user_id}/posts', response_model=PostInDB, status_code=status.HTTP_201_CREATED)
    async def create_post(self, body: CreatePost, current_active_self: UserModel = Depends(get_current_active_user_that_is_self)):
        """Create post

        Args:
            user_id (int): id of user in as saved in database

        Allowed roles:
        - All
        """
        post = PostService.create_post_for_user(body=body,
                                                user=current_active_self, db=self.db)
        return post

    @router.post('/users/{user_id}/posts/{post_id}/grant-access', response_model=List[UserAccessPostInDB], status_code=status.HTTP_201_CREATED)
    async def grant_access_to_post(self, post_id: int, body: UserIdList, current_active_self: UserModel = Depends(get_current_active_user_that_is_self)):
        """Grant access to users on own post

        Args:
            user_id (int): id of user in as saved in database
            post_id (int): post id of user id that you are granting access on

        Allowed roles:
        - All
        """
        accessList = UserAccessPostService.grant_access_to_post(
            post_id=post_id, user_id=current_active_self.id, user_ids=body.user_ids, db=self.db)

        return accessList
