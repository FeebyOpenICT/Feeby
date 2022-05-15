from Models import FileModel
from Exceptions import UnexpectedInstanceError
from sqlalchemy.orm import Session
from .RepositoryBase import RepositoryBase


class FileRepository(RepositoryBase):
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
