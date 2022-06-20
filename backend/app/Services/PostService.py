from typing import List, Optional
from sqlalchemy.orm import Session
from Exceptions import NotFoundException
from Exceptions.NoPermissions import NoPermissions
from Models import FeedbackModel, PostModel, RevisionModel, UserModel
from Repositories import PostRepository, RevisionRepository, FeedbackRepository
from Schemas import CreatePost
from Services import AspectService, RatingService
from .AspectRatingService import AspectRatingService


class PostService:
    @staticmethod
    def get_post_by_id(post_id: int, db: Session) -> Optional[PostModel]:
        """get post by id

        Args:
            post_id (int): id of post
            db (Session): database session

        Returns:
            Optional[PostModel]: post as saved in database or None
        """
        result = PostRepository.get_by_id(db=db, id=post_id)
        return result

    @staticmethod
    def get_post_by_id_or_fail(post_id: int, db: Session) -> PostModel:
        """get post by id or fail

        Args:
            post_id (int): id of post 
            db (Session): database session

        Raises:
            NotFoundException: if post is not found

        Returns:
            PostModel: post as saved in database
        """
        result = PostRepository.get_by_id(db=db, id=post_id)

        if not result:
            raise NotFoundException(resource="post", id=post_id)

        return result

    @staticmethod
    def get_posts_from_user_by_id_and_current_user_id(user_id: int, current_user_id: int, db: Session) -> List[PostModel]:
        """get posts from user that current user has access to whilst checking if user is self

        Args:
            current_user_id (int): id of current user that is requesting the posts from the user that they have access to
            user_id (int): owner of all the posts
            db (Session): database session

        Returns:
            List[PostModel]: list off all posts that current user has access to that belong to user
        """
        if user_id == current_user_id:
            posts = PostRepository.get_posts_from_user_by_id(
                user_id=user_id, db=db)
        else:
            posts = PostRepository.get_posts_with_access(
                current_user_id=current_user_id, user_id=user_id, db=db)
        return posts

    @staticmethod
    def create_post_for_user(body: CreatePost, user: UserModel, db: Session) -> PostModel:
        """Create post for user

        Args:
            body (CreatePost): body of create post call that has 
            user (UserModel): user model class as saved in database
            db (Session): database session

        Returns:
            PostModel: post as saved in database
        """
        post = PostModel(title=body.title,
                         description=body.description, user=user)
        PostRepository.save(post=post, db=db)

        revision = RevisionModel(
            description=body.revision.description, post=post)
        RevisionRepository.save(revision=revision, db=db)

        for item in body.revision.feedback:
            # check if aspect and rating are matched
            AspectRatingService.get_aspect_rating_or_fail(
                aspect_id=item.aspect_id, rating_id=item.rating_id, db=db)

            rating = RatingService.get_rating_by_id_or_fail(
                db=db, id=item.rating_id)
            aspect = AspectService.get_aspect_by_id_or_fail(
                id=item.aspect_id, db=db)

            feedback = FeedbackModel(
                description=item.description, aspect=aspect, rating=rating, revision=revision, reviewer=user)
            FeedbackRepository.save(feedback=feedback, db=db)

        return post

    @staticmethod
    def get_post_by_id_from_user_id(post_id: int, user_id: int, db: Session) -> Optional[PostModel]:
        """Get post by id created by user id

        Args:
            post_id (int): id of post
            user_id (int): id of owner a.k.a. creator of post
            db (Session): database session

        Returns:
            Optional[PostModel]: post as saved in database or None
        """
        post = PostRepository.get_post_by_id_by_user_id(
            post_id=post_id, user_id=user_id, db=db)
        return post

    @staticmethod
    def get_post_by_id_from_user_id_or_fail(post_id: int, user_id: int, db: Session) -> PostModel:
        """Get post by id created by user id or fail

        Args:
            post_id (int): id of post
            user_id (int): id of owner a.k.a. creator of post
            db (Session): database session

        Returns:
            PostModel: post as saved in database
        """
        post = PostRepository.get_post_by_id_by_user_id(
            post_id=post_id, user_id=user_id, db=db)

        if not post:
            raise NotFoundException(resource="post", id=post_id)

        return post

    @staticmethod
    def get_post_with_access(current_user_id: int, post_id: int, db: Session) -> Optional[PostModel]:
        """Get post from user_id by post_id with access as current_user_id

        Args:
            current_user_id (int): id of the current user trying to access post of user_id
            post_id (int): id of the post
            db (Session): database session

        Returns:
            Optional[PostModel]: returns post if post exists and current user has access or None 
        """
        post = PostRepository.get_post_with_access(
            current_user_id=current_user_id, post_id=post_id, db=db)
        return post

    @staticmethod
    def get_post_with_access_or_fail(current_user_id: int, post_id: int, db: Session) -> PostModel:
        post = PostRepository.get_post_with_access(
            current_user_id=current_user_id, post_id=post_id, db=db
        )

        if not post:
            raise NoPermissions(resource="post", id=post_id)

        return post
