from Models import FileModel
from Exceptions import UnexpectedInstanceError
from sqlalchemy.orm import Session
from .RepositoryBase import RepositoryBase
from fastapi import FastAPI, UploadFile
import shutil
from pathlib import Path


class FileRepository(RepositoryBase):
    @staticmethod
    def save_file_to_disk(upload_file: UploadFile, destination: Path):
        """create file

        Args:
            upload_file (UploadFile): file that has been uploaded
            destination (str): destination of the file
        Returns:
            filename (str): name of the file
            content_type (str): content_type of the file
            destination (str): location of the file
        """
        try:
            with destination.open("wb") as buffer:
                shutil.copyfileobj(upload_file.file, buffer)
        finally:
            upload_file.file.close()
        return{"filename": upload_file.filename, "content_type": upload_file.content_type, "destination": destination}

    @staticmethod
    def save(db: Session, file: FileModel) -> FileModel:
        """Save file instance in database

        Args:
            file (FileModel): file model
            db (Session): database session

        Raises:
            UnexpectedInstanceError: if file is not FileModel instance

        Returns:
            FileModel: file as saved in database
        """
        if not isinstance(file, FileModel):
            raise UnexpectedInstanceError

        db.add(file)
        db.flush()
        db.refresh(file)

        return file
