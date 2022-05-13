from typing import List
from fastapi import Depends
from Auth.validate_user import get_current_active_user, get_current_active_user_that_is_self
from Models import UserModel
from Schemas.FeedbackSchema import FeedbackInDB
from Services import PostService, UserService, RevisionService
from Schemas import CreateFeedback
from sqlalchemy.orm import Session
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from Services import FeedbackService

from database import get_db_connection

router = InferringRouter(
    tags=["Feedback"]
)


@cbv(router)
class FeedbackController:
    def __init__(
        self,
        post_id: int,
        user_id: int,
        revision_id: int,
        db: Session = Depends(get_db_connection),
    ) -> None:
        self.db = db
        self.user_id = user_id
        self.post_id = post_id
        self.revision_id = revision_id

        self.user = UserService.get_active_user_by_id_or_fail(
            id=user_id, db=db)
        self.post = PostService.get_post_by_id_or_fail(post_id=post_id, db=db)
        self.revision = RevisionService.get_revision_by_id_or_fail(
            id=revision_id, db=db)

    @router.post('/users/{user_id}/posts/{post_id}/revisions/{revision_id}/feedback', response_model=List[FeedbackInDB])
    async def create_feedback(self, body: List[CreateFeedback], current_active_user: UserModel = Depends(get_current_active_user)):
        feedback = FeedbackService.create_feedback(
            reviewer=current_active_user, owner=self.user, post=self.post, revision=self.revision, body=body, db=self.db)
        return feedback
