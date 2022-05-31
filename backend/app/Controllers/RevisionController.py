from fastapi import Depends, status, HTTPException, UploadFile, Form, File
from typing import List, Optional
from Schemas import RevisionInDB, FileInDB
from Schemas.RevisionSchema import CreateRevision
from Services import PostService, FileService
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
    def __init__(
            self,
            user_id: int,
            post_id: int,
            revision_id: Optional[int],
            db: Session = Depends(get_db_connection),
            current_active_user: UserModel = Depends(get_current_active_user),
    ) -> None:
        self.user_id = user_id
        self.revision_id = revision_id
        self.db = db
        self.current_active_user = current_active_user
        self.post_id = post_id
        self.feedback = None

        self.revision = RevisionService.get_revision_by_id_or_fail(revision_id=revision_id, db=db)
        self.post = PostService.get_post_by_id_or_fail(
            post_id=post_id, db=db)

        if user_id != current_active_user.id:
            user = UserService.get_active_user_by_id_or_fail(id=user_id, db=db)
            self.user = user
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

    @router.post('/users/{user_id}/posts/{post_id}/revisions', status_code=status.HTTP_201_CREATED,
                 response_model=RevisionInDB)
    async def create_revision(self, body: CreateRevision,
                              current_active_self: UserModel = Depends(get_current_active_user_that_is_self)):
        """Create revision

        Args:
            body (CreateRevision) ; description
            user_id (int): id of user in as saved in database
            post_id (int): post id of post you are creating revision for



        Allowed roles:
        - All
        """

        result = RevisionService.create_revision(
            user=current_active_self, body=body,
            post=self.post, db=self.db)
        return result

    @router.post('/users/{user_id}/posts/{post_id}/revisions/{revision_id}/files', status_code=status.HTTP_201_CREATED,
                 response_model=FileInDB)
    async def create_revision_file(self, files: List[UploadFile]):
        """Create revision file

        Args:
            files (UploadFile): List of uploaded files


        Allowed roles:
        - All
        """
        files = FileService.create_file(files=files, feedback=self.feedback, revision=self.revision_id, db=self.db)
        return files
