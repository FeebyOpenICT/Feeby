from fastapi import Depends, status, UploadFile
from typing import List
from Services.FileService import FileService
from Auth.validate_user import get_current_active_user_that_is_self
from Models.UserModel import UserModel
from Schemas.FileSchema import FileInDB, CreateFile
from fastapi_utils.inferring_router import InferringRouter


router = InferringRouter(
    tags=["Files"]
)


@router.post('/users/{user_id}/files', status_code=status.HTTP_201_CREATED,
             response_model=FileInDB)
async def create_file(self, body: CreateFile, files: List[UploadFile],
                          current_self_user: UserModel = Depends(get_current_active_user_that_is_self)):
    """Create revision

    Args:
        body (CreateFile): Revision or Feedback id
        files (UploadFile): Uploaded files


    Allowed roles:
    - All
    """

    result = FileService.create_file(
        files=files, db=self.db, revision=body.revision_id, feedback=body.feedback_id)
    return result
