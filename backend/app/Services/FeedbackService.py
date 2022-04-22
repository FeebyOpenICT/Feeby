from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from Models.PostModel import PostModel
from Models.UserModel import UserModel
from Repositories import FeedbackRepository
from Models import FeedbackModel
from Exceptions import NotFoundException
from Services import AspectRatingService, RatingService, AspectService


class FeedbackService:
    def get_by_id_or_fail(id: int, db: Session) -> FeedbackModel:
        feedback = FeedbackRepository.get_by_id(id=id, db=db)

        if not feedback:
            raise NotFoundException(resource="feedback", id=id)

        return feedback

    def create_feedback(
        description: str,
        post: PostModel,
        reviewer: UserModel,
        rating_id: int,
        aspect_id: int,
        reviewed_feedback_id: Optional[int],
        db: Session
    ):
        rating = RatingService.get_rating_by_id_or_fail(db=db, id=rating_id)
        aspect = AspectService.get_aspect_by_id_or_fail(db=db, id=aspect_id)

        if not AspectRatingService.get_aspect_rating_or_fail(aspect_id=aspect_id, rating_id=rating_id, db=db):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="rating and aspect are not coupled")

        reviewed_feedback = None

        if reviewed_feedback_id:
            reviewed_feedback = FeedbackService.get_by_id_or_fail(
                id=reviewed_feedback_id, db=db)

        feedback = FeedbackModel(
            description=description, post=post, reviewer=reviewer, rating=rating, aspect=aspect, reviewed_feedback=reviewed_feedback)

        feedback = FeedbackRepository.save(feedback=feedback, db=db)

        return feedback

    @staticmethod
    def create_multiple_feedback(
        post: PostModel,

    ):
        pass
