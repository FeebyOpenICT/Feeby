from typing import List
from fastapi import Depends
from Auth.validate_user import get_current_active_user, get_current_active_user_that_is_self
from Models import UserModel
from Services import PostService, UserService, RevisionService
from Schemas import FeedbackInDB, CreateFeedback
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

    @router.post('/users/{user_id}/posts/{post_id}/revisions/{revision_id}/feedback')
    async def create_feedback(self):
        return "hello world!"
