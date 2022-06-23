from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from Exceptions import NotFoundException
from Models import UserModel, RevisionModel
from Repositories import RevisionRepository
from Schemas import CreateRevision
from Services import PostService


class RevisionService:
    @staticmethod
    def create_revision(post_id: int, user: UserModel, body: CreateRevision, db: Session) -> RevisionModel:
        """create revision

        Args:
            user (UserModel): user that is trying to create revision on post
            body (CreateRevision): description of revision
            post_id (int): id of post as saved in database
            db (Session): database session

        Raises:
            NoPermissions: if post does not belong to user

        Returns:
            RevisionModel: created revision as saved in database (transactional)
        """
        post = PostService.get_post_by_id_or_fail(post_id=post_id, db=db)

        if post.user_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not allowed to create a revision on someone else's post")
        revision = RevisionModel(description=body.description, post=post)
        revision = RevisionRepository.save(db=db, revision=revision)
        return revision

    @staticmethod
    def get_all_revisions_from_post(db: Session, post_id: int) -> List[RevisionModel]:
        """get all revisions from post

        Args:
            post_id (int): post_id as saved in database
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
    def get_revision_by_id_or_fail(revision_id: int, db: Session) -> RevisionModel:
        """get revision by id or raise not found exception

        Args:
            revision_id (int): id of revision
            db (Session): database session

        Raises:
            NotFoundException: if revision not found

        Returns:
            RevisionModel: revision as saved in database
        """
        revision = RevisionRepository.get_by_id(id=revision_id, db=db)

        if not revision:
            raise NotFoundException(resource="revision", id=revision_id)

        return revision
