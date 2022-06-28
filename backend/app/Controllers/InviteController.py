from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Auth.validate_user import get_current_active_user
from Models import UserModel
from Schemas import RequestedFeedbackInDB, CreateRequestedFeedback
from Services import InviteService
from database import get_db_connection

router = APIRouter(
    # prefix="/",
    tags=["Invitations"]
)


@router.post('/revisions/{revision_id}/invite', response_model=List[RequestedFeedbackInDB])
async def invite_on_revision(
        revision_id: int,
        body: CreateRequestedFeedback,
        current_active_user: UserModel = Depends(get_current_active_user),
        db: Session = Depends(get_db_connection)
):
    """Invite user to give feedback on revision

    Allowed roles:
    - All
    """
    result = InviteService.invite_users_on_revision(revision_id=revision_id,
                                                    potential_owner_of_revision=current_active_user,
                                                    users_to_invite=body.users, db=db)
    return result


@router.get('/revisions/{revision_id}/invites', response_model=List[RequestedFeedbackInDB])
async def get_invites_on_revision(
        revision_id: int,
        current_active_user: UserModel = Depends(get_current_active_user),
        db: Session = Depends(get_db_connection)
):
    """Check which users have been invited

    Args:
        revision_id: id of revision

    Returns:
        List of users that have been invited
    """
    result = InviteService.get_invited_users_on_revision(revision_id=revision_id,
                                                         potential_owner_of_revision=current_active_user, db=db)
    return result
