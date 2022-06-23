import collections
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from Exceptions import NotFoundException
from Models import FeedbackModel, RevisionModel, UserModel
from Repositories import FeedbackRepository
from Schemas import CreateFeedback
from Services import AspectRatingService, AspectService, RatingService, \
    UserAccessPostService


class FeedbackService:
    @staticmethod
    def create_feedback(
            reviewer: UserModel,
            revision: RevisionModel,
            body: List[CreateFeedback],
            db: Session
    ) -> List[FeedbackModel]:
        if reviewer.id == revision.post.user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not allowed to give oneself feedback")

        UserAccessPostService.check_access_to_post_or_fail(
            post_id=revision.post.id, user_id=reviewer.id, db=db)

        for feedback in revision.feedback:
            if feedback.reviewer.id == reviewer.id:
                raise HTTPException(status.HTTP_409_CONFLICT, "User has already given feedback on this revision")

        baseline_measurement_aspect_ids = [
            fb.aspect_id for fb in FeedbackRepository.get_baseline_measurement(post_id=revision.post.id, db=db)]

        sent_aspect_ids = [fb.aspect_id for fb in body]

        if not collections.Counter(baseline_measurement_aspect_ids) == collections.Counter(sent_aspect_ids):
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                                detail="aspects that were graded do not match baseline measurement from student.")

        feedback = []

        for item in body:
            AspectRatingService.get_aspect_rating_or_fail(
                aspect_id=item.aspect_id, rating_id=item.rating_id, db=db)
            aspect = AspectService.get_aspect_by_id_or_fail(
                id=item.aspect_id, db=db)
            rating = RatingService.get_rating_by_id_or_fail(
                id=item.rating_id, db=db)
            feedback.append(
                FeedbackRepository.save(
                    feedback=FeedbackModel(description=item.description, rating=rating,
                                           aspect=aspect, revision=revision, reviewer=reviewer),
                    db=db
                )
            )

        return feedback

    @staticmethod
    def get_feedback_by_id_or_fail(feedback_id: int, db: Session) -> FeedbackModel:
        """get feedback by id or raise not found exception

        Args:
            feedback_id (int): id of feedback
            db (Session): database session

        Raises:
            NotFoundException: if feedback not found

        Returns:
            FeedbackModel: feedback as saved in database
        """
        feedback = FeedbackRepository.get_by_id(id=feedback_id, db=db)

        if not feedback:
            raise NotFoundException(resource="feedback", id=feedback_id)

        return feedback
