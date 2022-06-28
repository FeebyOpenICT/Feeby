from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from Exceptions import DuplicateKey
from Exceptions.NoPermissions import NoPermissions
from Models import UserModel, RequestedFeedbackModel
from Repositories import RequestedFeedbackRepository
from Schemas import UserPublicInDB
from .RevisionService import RevisionService
from .UserService import UserService


class InviteService:
    @staticmethod
    def invite_users_on_revision(revision_id: int, owner_of_revision: UserModel,
                                 users_to_invite: List[UserPublicInDB],
                                 db: Session):
        revision = RevisionService.get_revision_by_id_or_fail(revision_id=revision_id, db=db)

        if revision.post.user_id is not owner_of_revision.id:
            NoPermissions(resource="revision", id=revision_id)

        user_ids = [user.id for user in users_to_invite]

        if revision.post.user_id in user_ids:
            raise HTTPException(422, 'Can not invite self for feedback')

        requested_feedback_models = []

        for user_id in user_ids:
            if RequestedFeedbackRepository.get_by_id(user_id=user_id, revision_id=revision_id, db=db):
                raise DuplicateKey(resource='Already requested feedback from user', id=user_id)

            user = UserService.get_user_by_id_or_fail(id=user_id, db=db)
            requested_feedback = RequestedFeedbackRepository.save(
                requested_feedback=RequestedFeedbackModel(revision=revision, user=user), db=db)
            requested_feedback_models.append(requested_feedback)

        return requested_feedback_models
