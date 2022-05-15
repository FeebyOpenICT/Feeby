from sqlalchemy.orm import Session
from Models import FileModel, RevisionModel
from Repositories import FileRepository
from fastapi import FastAPI, UploadFile


class FileService:
    @staticmethod
    def create_file(filename: str, content_type: str, location: str, revision: RevisionModel, db: Session) -> FileModel:
        """create file

        Args:
            filename (str): name of the file
            content_type (str): content type of the file
            location (str): location of the file
            revision (RevisionModel): revision file has been added too
            db (Session): database session
        """

        # alright so i gotta make it so a file can be uploaded
        # i then have to make it so we can get the filename content & loacation
        # and all of that needs to be the filemodel so it can be saved

        file = FileModel(filename=filename, content_type=content_type, location=location, revision=revision)
        file = FileRepository.save(db=db, file=file)
        return file
