from typing import List, Optional
from .RepositoryBase import RepositoryBase
from sqlalchemy.orm import Session
from Models import RevisionModel
from Exceptions import UnexpectedInstanceError


class RevisionRepository(RepositoryBase):
    @staticmethod
    def get_all(db: Session) -> List[RevisionModel]:
        """get all revisions

        Args:
            db (Session): database session

        Returns:
            List[RevisionModel]: list of all revisions from db
        """
        result = db.query(RevisionModel).all()
        return result

    @staticmethod
    def get_by_id(db: Session, id: int) -> Optional[RevisionModel]:
        """get revision by id

        Args:
            db (Session): database session
            id (int): id of revision

        Returns:
            Optional[RevisionModel]: Revision as saved in database or none
        """

        result = db.query(RevisionModel).filter(RevisionModel.id == id).first()
        return result

    def save(db: Session, revision: RevisionModel) -> RevisionModel:
        """save revision in db

        Args:
            db (Session): database session
            revision (RevisionModel): revision model to save in db

        Raises:
            UnexpectedInstanceError: raised if instance is not of type RevisionModel

        Returns:
            RevisionModel: revision as saved in database
        """
        if not isinstance(revision, RevisionModel):
            raise UnexpectedInstanceError

        db.add(revision)
        db.flush()
        db.refresh(revision)

        return revision

    @staticmethod
    def get_revisions_from_post(post_id: int, db: Session) -> List[RevisionModel]:
        """get revisions from post

        Args:
            post_id (int): id of post
            db (Session): database session

        Returns:
            List[RevisionModel]: list of revisions from post
        """
        result = db.query(RevisionModel).filter(
            RevisionModel.post_id == post_id).all()
        return result
