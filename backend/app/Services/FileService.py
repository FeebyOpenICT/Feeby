import pathlib
import uuid
from pathlib import Path
from typing import List, Optional

from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from Models import FileModel, UserModel
from Repositories import FileRepository
from Services import RevisionService, FeedbackService


class FileService:
    @staticmethod
    def create_files(files: List[UploadFile], db: Session, user: UserModel, revision_id: Optional[int] = None,
                     feedback_id: Optional[int] = None
                     ) -> FileModel:
        """create file

        Args:
            files(UploadFile): all uploaded files
            revision_id (int): revision id as saved in database
            feedback_id (int): feedback id as saved in database
            db (Session): database session

        Returns:
            Filemodel: file as saved in database
        """
        if feedback_id and revision_id:
            raise ValueError("You can only pass either feedback_id or revision_id, not both")

        if revision_id:
            revision = RevisionService.get_revision_by_id_or_fail(revision_id=revision_id, db=db)
            if revision.post.user_id != user.id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                    detail="Not allowed to create files on a revision on someone else's post")

        if feedback_id:
            feedback = FeedbackService.get_feedback_by_id_or_fail(feedback_id=feedback_id, db=db)
            if feedback.reviewer_id == user.id:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                    detail="Not allowed to create files on someone else's feedback")

        for file in files:
            file.filename = str(uuid.uuid4().hex) + \
                            pathlib.Path(file.filename).suffix

            file_on_disk = FileRepository.save_file_to_disk(
                upload_file=file, destination=Path(f'./files/{file.filename}'))

            location = file_on_disk.get("destination").absolute().as_posix()

            saved_db_file = FileRepository.save(
                db=db,
                file=FileModel(filename=file_on_disk["filename"],
                               content_type=file_on_disk["content_type"],
                               location=location,
                               revision=revision,
                               feedback=feedback)
            )

            return saved_db_file
