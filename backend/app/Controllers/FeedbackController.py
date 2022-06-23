from typing import List

from fastapi import Depends, UploadFile, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session

from Auth.validate_user import get_current_active_user
from Models import UserModel
from Schemas import CreateFeedback, FileInDB
from Schemas.FeedbackSchema import FeedbackInDB
from Services import FeedbackService, FileService
from Services import RevisionService
from database import get_db_connection

router = InferringRouter(
    tags=["Feedback"]
)


@cbv(router)
class FeedbackController:
    def __init__(
            self,
            revision_id: int,
            db: Session = Depends(get_db_connection),
            current_active_user: UserModel = Depends(get_current_active_user)
    ) -> None:
        self.db = db
        self.revision_id = revision_id
        self.current_active_user = current_active_user

        self.revision = RevisionService.get_revision_by_id_or_fail(
            revision_id=revision_id, db=db)

    @router.post('/revisions/{revision_id}/feedback', response_model=List[FeedbackInDB])
    async def create_feedback(self, body: List[CreateFeedback]):
        feedback = FeedbackService.create_feedback(
            reviewer=self.current_active_user, revision=self.revision, body=body,
            db=self.db)
        return feedback

    @router.post('/feedback/{feedback_id}/files',
                 status_code=status.HTTP_201_CREATED, response_model=FileInDB)
    async def create_revision_file(self, feedback_id: int, files: List[UploadFile]):
        """Create revision file

        Args:
            feedback_id (int): Feedback id as saved in db
            files (UploadFile): List of uploaded files


        Allowed roles:
        - All
        """
        files = FileService.create_files(files=files, feedback_id=feedback_id, user=self.current_active_user,
                                         db=self.db)
        return files
