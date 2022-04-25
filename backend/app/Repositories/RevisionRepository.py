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

        return revision
