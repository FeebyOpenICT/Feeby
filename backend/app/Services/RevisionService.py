from typing import List, Optional
from fastapi import HTTPException, status, UploadFile
from sqlalchemy.orm import Session
from Models import UserModel, PostModel, RevisionModel
from Repositories import RevisionRepository
from Services import FileService


class RevisionService:
    @staticmethod
    def create_revision(post: PostModel, files: List[UploadFile], description: str, db: Session) -> RevisionModel:
        """create revision

        Args:
            post (PostModel): post as saved in database
            db (Session): database session
        """
        revision = RevisionModel(description=description, post=post)
        revision = RevisionRepository.save(db=db, revision=revision)
        for file in files:
            FileService.create_file(file=file, revision_id=revision.id, db=db)
        return revision

    @staticmethod
    def get_all_revisions_from_post(db: Session, post_id: int) -> List[RevisionModel]:
        """get all revisions from post

        Args:
            db (Session): database session
        """
        revisions = RevisionRepository.get_revisions_from_post(
            post_id=post_id, db=db)
        return revisions
