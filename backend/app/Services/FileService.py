import pathlib

from sqlalchemy.orm import Session
from Models import FileModel, RevisionModel, FeedbackModel
from Repositories import FileRepository
from fastapi import UploadFile
from pathlib import Path
import uuid
from typing import List, Optional


class FileService:
    @staticmethod
    def create_file(files: List[UploadFile], revision: Optional[int], feedback: Optional[int],
                    db: Session) -> FileModel:
        """create file

        Args:
            files(UploadFile): all uploaded files
            revision (int): revision id as saved in database
            feedback(int): feedback id as saved in database
            db (Session): database session
        """
        if feedback:
            revision = None
        else:
            feedback = None

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
