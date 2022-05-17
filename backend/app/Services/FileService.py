from sqlalchemy.orm import Session
from Models import FileModel, RevisionModel
from Repositories import FileRepository
from fastapi import UploadFile
from pathlib import Path


class FileService:
    @staticmethod
    def create_file(file: UploadFile, revision_id: int, db: Session) -> FileModel:
        """create file

        Args:
            file(UploadFile): name of the file
            revision_id (int): revision id as saved in database
            db (Session): database session
        """
        file_on_disk = FileRepository.save_file_to_disk(upload_file=file, destination=Path('files'))
        file = FileModel(filename=file_on_disk["filename"], content_type=file_on_disk["content_type"], location=file_on_disk["destination"], revision=None)
        file.revision_id = revision_id
        file = FileRepository.save(db=db, file=file)
        return file
