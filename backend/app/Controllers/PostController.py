from fastapi import APIRouter, Depends, Security, status
from typing import List
from Exceptions.NotFound import NotFound
from Services.PostService import PostService
from Auth.validate_user import get_current_active_user
from sqlalchemy.orm import Session
from Schemas.PostSchema import CreatePost, GrantAccessToPost
from database import get_db_connection
from Models.Role import Roles
from Models.UserModel import UserModel
from Schemas.PostSchema import PostInDB
from fastapi_utils.cbv import cbv
from Services.UserService import UserService

router = APIRouter(
    tags=["Posts"]
)


@cbv(router)
class PostController:
    def __init__(
        self,
        user_id: int,
        db: Session = Depends(get_db_connection),
        current_active_user: UserModel = Security(
            get_current_active_user,
            scopes=[
            Roles.STUDENT['title'],
            Roles.ADMIN['title'],
            Roles.INSTRUCTOR['title'],
            Roles.CONTENT_DEVELOPER['title'],
            Roles.TEACHING_ASSISTANT['title'],
            ]
        )
    ) -> None:
        self.user_id = user_id
        self.db = db
        self.current_active_user = current_active_user

        if user_id == current_active_user.id:
            self.user = current_active_user
        else:
            user = UserService.get_user_by_id(id=user_id, db=db)

            if user is None:
                raise NotFound("user", user_id)

            self.user = user

    @router.get('/users/{user_id}/posts',  response_model=List[PostInDB])
    async def get_posts(self):
        """
        Read post from user_id

        Allowed roles: admin, instructor, student, content_developer, teaching_assistant
        """
        result = PostService.get_posts_from_user_by_id(
            user_id=self.user_id, db=self.db)
        return result

    @router.post('/users/{user_id}/posts', response_model=PostInDB, status_code=status.HTTP_201_CREATED)
    async def create_post(self, body: CreatePost):
        """
        Create post

        Allowed roles: admin, instructor, student, content_developer, teaching_assistant
        """
        post = PostService.create_post_for_user_by_model(title=body.title, description=body.description,
                                                         user=self.user, db=self.db)
        return post

    @router.patch('/users/{user_id}/posts/{post_id}/grant-access', status_code=status.HTTP_201_CREATED)
    async def grant_access_to_post(self, post_id: int, body: GrantAccessToPost):
        return post_id
