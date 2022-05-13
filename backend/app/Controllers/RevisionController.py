from fastapi import Depends, status, HTTPException
from typing import List
from Schemas import RevisionInDB
from Schemas.RevisionSchema import CreateRevision
from Services import PostService
from Auth.validate_user import get_current_active_user, get_current_active_user_that_is_self
from sqlalchemy.orm import Session
from Services.RevisionService import RevisionService
from database import get_db_connection
from Models.UserModel import UserModel
from Schemas import CreateInitialRevision
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from Services.UserService import UserService

router = InferringRouter(
    tags=["Revisions"]
)


@cbv(router)
class RevisionController:

    def __init__(self, user_id: int, post_id: int, db: Session = Depends(get_db_connection)) -> None:
        self.user_id = user_id
        self.post_id = post_id
        self.db = db
        self.user = UserService.get_active_user_by_id_or_fail(
            id=user_id, db=db)
        self.post = PostService.get_post_by_id_or_fail(post_id=post_id, db=db)

    # @router.get('/users/{user_id}/posts/{post_id}/revisions', response_model=List[RevisionInDB])
    # async def get_revisions(self):
    #     """Get all revisions from database

    #     Args:
    #         user_id (int): id of user in as saved in database
    #         post_id (int): post id of post you are getting revisions from

    #     Allowed roles:
    #     - All
    #     """
    #     result = RevisionService.get_all_revisions_from_post(
    #         db=self.db, post_id=self.post_id)
    #     return result

    @router.post('/users/{user_id}/posts/{post_id}/revisions', status_code=status.HTTP_201_CREATED, response_model=RevisionInDB)
    async def create_revision(self, body: CreateRevision, current_active_self: UserModel = Depends(get_current_active_user_that_is_self)):
        """Create revision

        Args:
            user_id (int): id of user in as saved in database
            post_id (int): post id of post you are creating revision for

        Allowed roles:
        - All
        """
        result = RevisionService.create_revision(
            user=current_active_self,
            post=self.post, body=body, db=self.db)
        return result
