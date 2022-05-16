from sqlalchemy.orm import Session
from Models import FileModel, RevisionModel
from Repositories import FileRepository
from fastapi import FastAPI, UploadFile
import shutil
from pathlib import Path


class FileService:
    @staticmethod
    def save_file_to_disk(upload_file: UploadFile, location: Path):
        """create file

        Args:
            upload_file (object): file that has been uploaded
            location (str): location of the file
        Returns:
            filename (str): name of the file
            content_type (str): content_type of the file
            location (str): location of the file
        """
        try:
            with location.open("wb") as buffer:
                shutil.copyfileobj(upload_file.file, buffer)
        finally:
            upload_file.file.close()
        return{"filename": upload_file.filename, "content_type:": upload_file.content_type, location: Path}

    @staticmethod
    def create_file_in_db(filename: str, content_type: str, location: str, revision: RevisionModel, db: Session) -> FileModel:
        """create file

        Args:
            filename (str): name of the file
            content_type (str): content type of the file
            location (str): location of the file
            revision (RevisionModel): revision file has been added too
            db (Session): database session
        """
        file = FileModel(filename=filename, content_type=content_type, location=location, revision=revision)
        file = FileRepository.save(db=db, file=file)
        return file
