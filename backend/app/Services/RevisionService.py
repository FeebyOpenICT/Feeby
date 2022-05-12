from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Models import UserModel, PostModel, RevisionModel
from Repositories import RevisionRepository


class RevisionService:
    @staticmethod
    def create_revision(post: PostModel, description: str, db: Session) -> RevisionModel:
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
        """
        revisions = RevisionRepository.get_revisions_from_post(
            post_id=post_id, db=db)
        return revisions
