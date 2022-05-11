from typing import List
from .RepositoryBase import RepositoryBase
from sqlalchemy.orm import Session
from Models import RevisionModel
from Exceptions import UnexpectedInstanceError


class RevisionRepository(RepositoryBase):
    @staticmethod
    def get_all(db: Session):
        result = db.query(RevisionModel).all()
        return result

    @staticmethod
    def get_by_id(db: Session, id: int):
        result = db.query(RevisionModel).filter(RevisionModel.id == id).first()
        return result

    def save(db: Session, revision: RevisionModel) -> RevisionModel:
        if not isinstance(revision, RevisionModel):
            raise UnexpectedInstanceError

        db.add(revision)
        db.flush()
        db.refresh(revision)

        return revision

    @staticmethod
    def get_revisions_from_post(post_id: int, db: Session) -> List[RevisionModel]:
        result = db.query(RevisionModel).filter(
            RevisionModel.post_id == post_id).all()
        return result
