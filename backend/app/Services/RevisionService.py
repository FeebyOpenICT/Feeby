from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Models import UserModel, PostModel, RevisionModel
from Repositories import RevisionRepository
from Exceptions import NotFoundException, NoPermissions


class RevisionService:
    @staticmethod
    def create_revision(post: PostModel, user: UserModel, description: str, db: Session) -> RevisionModel:
        """create revision

        Args:
            post (PostModel): post as saved in database
            db (Session): database session

        Raises:
            NoPermissions: if post does not belong to user

        Returns:
            RevisionModel: created revision as saved in database (transactional)
        """
        if post.user_id != user.id:
            raise NoPermissions(resource="post", id=post.id)

        revision = RevisionModel(description=description, post=post)
        revision = RevisionRepository.save(db=db, revision=revision)
        return revision

    @staticmethod
    def get_all_revisions_from_post(db: Session, post_id: int) -> List[RevisionModel]:
        """get all revisions from post

        Args:
            db (Session): database session
            post_id (int): id of post

        Returns:
            List[RevisionModel]: list of revision belonging to post
        """
        revisions = RevisionRepository.get_revisions_from_post(
            post_id=post_id, db=db)
        return revisions

    @staticmethod
    def get_revision_by_id(id: int, db: Session) -> Optional[RevisionModel]:
        """get revision by id

        Args:
            id (int): id of revision
            db (Session): database session

        Returns:
            Optional[RevisionModel]: revision as saved in database or None
        """
        revision = RevisionRepository.get_by_id(id=id, db=db)
        return revision

    @staticmethod
    def get_revision_by_id_or_fail(id: int, db: Session) -> RevisionModel:
        """get revision by id or raise not found exception

        Args:
            id (int): id of revision
            db (Session): database session

        Raises:
            NotFoundException: if revision not found

        Returns:
            RevisionModel: revision as saved in database
        """
        revision = RevisionRepository.get_by_id(id=id, db=db)

        if not revision:
            raise NotFoundException(resource="revision", id=id)

        return revision
