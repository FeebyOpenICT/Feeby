from typing import List, Optional
from Exceptions import DuplicateKey, NotFoundException
from Models import PostModel, UserAccessPostModel, UserModel
from Repositories import PostRepository, UserAccessPostRepository, UserRepository
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


def get_posts_from_user_by_id_and_current_user_id(user_id: int, current_user_id: int, db: Session) -> List[PostModel]:
    """
    Gets all the posts from a user by their id

    user_id = integer equal to the the user id

    Returns a list of python Post mapped class from the database
    """
    if user_id == current_user_id:
        result = PostRepository.get_posts_from_user_by_id(
            user_id=user_id, db=db)
    else:
        result = PostRepository.get_posts_with_access(
            current_user_id=current_user_id, user_id=user_id, db=db)
    return result


def create_post_for_user_by_id(title: str, description: str, user_id: int, db: Session) -> PostModel:
    user = UserRepository.get_user_by_id(id=user_id, db=db)

    if user is None:
        raise NotFoundException(resource="user", id=user_id)

    post = PostRepository.create_post_for_user(
        title=title, description=description, user=user, db=db)

    return post


def create_post_for_user(title: str, description: str, user: UserModel, db: Session) -> PostModel:
    post = PostRepository.create_post_for_user(
        title=title, description=description, user=user, db=db)

    return post


def get_post_by_id(post_id: int, user_id: int, db: Session) -> Optional[PostModel]:
    post = PostRepository.get_post_by_id(
        post_id=post_id, user_id=user_id, db=db)
    return post


def grant_access_to_post(post_id: int, user_id: int, user_ids: List[int], db: Session) -> List[UserAccessPostModel]:
    post: Optional[PostModel] = PostRepository.get_post_by_id(
        post_id=post_id, user_id=user_id, db=db)

    if post is None:
        raise NotFoundException(resource="post", id=post_id)

    users = []

    for user_id in user_ids:
        user = UserRepository.get_user_by_id(id=user_id, db=db)

        if not user:
            raise NotFoundException(resource="user", id=user_id)

        users.append(user)
    try:
        accessList = UserAccessPostRepository.grant_access_to_users_to_post(
            post=post, users=users, db=db)

    except IntegrityError as error:
        raise DuplicateKey(resource="User Access Post",
                           id=error.params['user_id'])

    return accessList


def get_post_with_access(current_user_id: int, post_id: int, db: Session) -> Optional[PostModel]:
    """
    Get post that the current_user_id has access to

    returns None if the user does not have access to that post
    """
    result = PostRepository.get_post_with_access(
        current_user_id=current_user_id, post_id=post_id, db=db)
    return result
