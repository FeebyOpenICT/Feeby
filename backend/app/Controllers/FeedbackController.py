from typing import List
from fastapi import Depends
from Auth.validate_user import get_current_active_user
from Models import UserModel
from Services import PostService, UserService
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
        db: Session = Depends(get_db_connection),
        current_active_user: UserModel = Depends(get_current_active_user)
    ) -> None:
        if user_id != current_active_user.id:
            self.user = UserService.get_active_user_by_id_or_fail(
                id=user_id, db=db)
            self.post = PostService.get_post_with_access_or_fail(
                current_user_id=current_active_user.id, post_id=post_id, db=db)
        else:
            self.post = PostService.get_post_by_id_or_fail(
                post_id=post_id, user_id=user_id, db=db)
            self.user = current_active_user

        self.current_active_user = current_active_user
        self.db = db

    @router.post('/users/{user_id}/posts/{post_id}/feedback', response_model=FeedbackInDB)
    async def create_feedback(self, body: List[CreateFeedback]):
        # feedback = FeedbackService.create_multiple_feedback()
        return 'WIP'
