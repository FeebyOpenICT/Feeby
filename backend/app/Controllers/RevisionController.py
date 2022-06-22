from typing import List

from fastapi import Depends, status, UploadFile
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from Auth.validate_user import get_current_active_user
from Models.UserModel import UserModel
from Schemas import RevisionInDB, FileInDB
from Schemas.RevisionSchema import CreateRevision
from Services import PostService, FileService
from Services.RevisionService import RevisionService
from database import get_db_connection

router = InferringRouter(
    tags=["Revisions"]
)


@cbv(router)
class RevisionController:
    def __init__(
            self,
            post_id: int,
            db: Session = Depends(get_db_connection),
            current_active_user: UserModel = Depends(get_current_active_user),
    ) -> None:
        self.db = db
        self.current_active_user = current_active_user
        self.post_id = post_id

        self.post = PostService.get_post_by_id_or_fail(
            post_id=post_id, db=db)

        self.db = db
        self.post = PostService.get_post_by_id_or_fail(post_id=post_id, db=db)

    @router.post('/posts/{post_id}/revisions', status_code=status.HTTP_201_CREATED,
                 response_model=RevisionInDB)
    async def create_revision(self, body: CreateRevision):
        """Create revision

        Args:
            body (CreateRevision) ; description
            post_id (int): id of post you are creating revision for

        Allowed roles:
        - All
        """

        result = RevisionService.create_revision(
            user=self.current_active_user, body=body,
            post=self.post, db=self.db)
        return result

    @router.post('/posts/{post_id}/revisions/{revision_id}/files', status_code=status.HTTP_201_CREATED,
                 response_model=FileInDB)
    async def create_revision_file(self, revision_id: int, files: List[UploadFile]):
        """Create revision file

        Args:
            revision_id (int): revision id as saved in db
            files (UploadFile): List of uploaded files


        Allowed roles:
        - All
        """
        files = FileService.create_files(files=files, revision_id=revision_id, user=self.current_active_user,
                                         db=self.db)
        return files
