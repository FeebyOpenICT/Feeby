from typing import List
from fastapi import HTTPException, status
from Exceptions import NoPermissions, NotFoundException, DoesNotBelongTo
from sqlalchemy.orm import Session
from Models import FeedbackModel, PostModel, RevisionModel, UserModel
from Repositories import FeedbackRepository
from Schemas import CreateFeedback
from Services import PostService, RevisionService, AspectRatingService, AspectService, RatingService, UserAccessPostService
import collections


class FeedbackService:
    @staticmethod
    def create_feedback(
        reviewer: UserModel,
        owner: UserModel,
        post: PostModel,
        revision: RevisionModel,
        body: List[CreateFeedback],
        db: Session
    ) -> List[FeedbackModel]:
        if reviewer.id == owner.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Not allowed to give oneself feedback")

        UserAccessPostService.check_access_to_post_or_fail(
            post_id=post.id, user_id=reviewer.id, db=db)

        if post.user_id != owner.id:
            raise DoesNotBelongTo(
                parentResource="post", parentId=post.id, resource="user", id=owner.id)

        if revision.post_id != post.id:
            raise DoesNotBelongTo(
                parentResource="revision", parentId=revision.id, resource="post", id=post.id)

        baseline_measurement_aspect_ids = [
            fb.aspect_id for fb in FeedbackRepository.get_baseline_measurement(post_id=post.id, db=db)]

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
