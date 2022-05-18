import pathlib

from sqlalchemy.orm import Session
from Models import FileModel, RevisionModel
from Repositories import FileRepository
from fastapi import UploadFile
from pathlib import Path
import uuid


class FileService:
    @staticmethod
    def create_file(file: UploadFile, revision: RevisionModel, db: Session) -> FileModel:
        """create file

        Args:
            file(UploadFile): name of the file
            revision (RevisionModel): revision id as saved in database
            db (Session): database session
        """
        file.filename = str(uuid.uuid4().hex) + pathlib.Path(file.filename).suffix

        file_on_disk = FileRepository.save_file_to_disk(upload_file=file, destination=Path('./files'))

        location = file_on_disk.get("destination").absolute().as_posix()

        saved_db_file = FileRepository.save(
            db=db,
            file=FileModel(filename=file_on_disk["filename"],
                           content_type=file_on_disk["content_type"],
                           location=location,
                           revision=revision)
        )

        return saved_db_file
