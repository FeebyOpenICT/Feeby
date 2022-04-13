from typing import List, Optional
from sqlalchemy.orm import Session
from Exceptions import DuplicateKey, NotFound
from Models import PostModel, UserAccessPostModel, UserModel
from Repositories import PostRepository, UserAccessPostRepository, UserRepository
from sqlalchemy.exc import IntegrityError


class PostService:
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
            result = PostRepository.get_posts_from_user_by_id(
                user_id=user_id, db=db)
        else:
            result = PostRepository.get_posts_with_access(
                current_user_id=current_user_id, user_id=user_id, db=db)
        return result

    @staticmethod
    def create_post_for_user_by_id(title: str, description: str, user_id: int, db: Session) -> PostModel:
        """Create post for user by id

        Args:
            title (str): title of post  
            description (str): description of post
            user_id (int): id of user that the post will belong to
            db (Session): database session

        Raises:
            NotFound: if user is not found

        Returns:
            PostModel: post as saved in database
        """
        user = UserRepository.get_user_by_id(id=user_id, db=db)

        if user is None:
            raise NotFound(resource="user", id=user_id)

        post = PostRepository.create_post_for_user(
            title=title, description=description, user=user, db=db)

        return post

    @staticmethod
    def create_post_for_user_by_model(title: str, description: str, user: UserModel, db: Session) -> PostModel:
        """Create post for user

        Args:
            title (str): title of post  
            description (str): description of post
            user (UserModel): user model class as saved in database
            db (Session): database session

        Returns:
            PostModel: post as saved in database
        """
        post = PostRepository.create_post_for_user(
            title=title, description=description, user=user, db=db)

        return post

    @staticmethod
    def get_post_by_id(post_id: int, user_id: int, db: Session) -> Optional[PostModel]:
        """Get post by id created by user id

        Args:
            post_id (int): id of post
            user_id (int): id of owner a.k.a. creator of post
            db (Session): database session

        Returns:
            Optional[PostModel]: post as saved in database or None
        """
        post = PostRepository.get_post_by_id(
            post_id=post_id, user_id=user_id, db=db)
        return post

    @staticmethod
    def grant_access_to_post(post_id: int, user_id: int, user_ids: List[int], db: Session) -> List[UserAccessPostModel]:
        """Grant access to post id owned by user id to user ids

        Args:
            post_id (int): id of post
            user_id (int): id of owner of post
            user_ids (List[int]): list of ids of users that should get access to posts
            db (Session): _description_

        Raises:
            NotFound: if post is not found by post_id owned by user_id
            NotFound: if any user is not found in user_ids
            DuplicateKey: if any user from user_ids already has access to post_id by user_id

        Returns:
            List[UserAccessPostModel]: list of newly created access models
        """
        post: Optional[PostModel] = PostRepository.get_post_by_id(
            post_id=post_id, user_id=user_id, db=db)

        if post is None:
            raise NotFound(resource="post", id=post_id)

        users = []

        for user_id in user_ids:
            user = UserRepository.get_user_by_id(id=user_id, db=db)

            if not user:
                raise NotFound(resource="user", id=user_id)

            users.append(user)
        try:
            accessList = UserAccessPostRepository.grant_access_to_users_to_post(
                post=post, users=users, db=db)

        except IntegrityError as error:
            raise DuplicateKey(resource="User Access Post",
                               id=error.params['user_id'])

        return accessList

    @staticmethod
    def get_post_with_access(current_user_id: int, user_id: int, post_id: int, db: Session) -> Optional[PostModel]:
        """Get post from user_id by post_id with access as current_user_id

        Args:
            current_user_id (int): id of the current user trying to access post of user_id
            user_id (int): id of owner of the post
            post_id (int): id of the post
            db (Session): database session

        Returns:
            Optional[PostModel]: returns post if post exists and current user has access or None 
        """
        result = PostRepository.get_post_with_access(
            current_user_id=current_user_id, post_id=post_id, db=db)
        return result
