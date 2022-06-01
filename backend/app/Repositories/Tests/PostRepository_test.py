from datetime import datetime
from sqlalchemy import null
from sqlalchemy.orm import Session
from Models import PostModel, UserAccessPostModel, UserModel
from Repositories import PostRepository, RoleRepository
from Schemas import RolesEnum
from Services import PostService, RoleService


def test_get_posts_from_user_by_id(db: Session, current_active_user: UserModel):
    post1 = PostModel(title="title", description="hello",
                      user=current_active_user)
    post2 = PostModel(title="title2", description="hello2",
                      user=current_active_user)
    db.add_all([post1, post2])
    db.commit()

    posts = PostRepository.get_posts_from_user_by_id(
        user_id=current_active_user.id, db=db)

    assert len(posts) == 2
    assert posts[0] == post1
    assert posts[1] == post2


def test_create_post_for_user(db: Session, current_active_user: UserModel):
    title = "title"
    description = "askljdhf"

    post = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)

    assert post.user == current_active_user
    assert post.description == description
    assert isinstance(post.time_created, datetime)
    assert isinstance(post.time_updated, datetime)
    assert isinstance(post.id, int)


def test_get_post_by_id(db: Session, current_active_user: UserModel):
    title = "title"
    description = "askljdhf"

    postCreated = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)

    post = PostRepository.get_post_by_id_by_user_id(
        post_id=postCreated.id, user_id=current_active_user.id, db=db)

    assert post.user == current_active_user
    assert post.description == description
    assert isinstance(post.time_created, datetime)
    assert isinstance(post.time_updated, datetime)
    assert isinstance(post.id, int)
    assert post == postCreated


def test_get_post_with_access(db: Session, current_active_user: UserModel):
    # create posts
    title = "title"
    description = "askljdhf"

    postCreated = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)
    postCreated2 = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)

    # create user
    user2 = UserModel("lisa", "lasdhf", 23, False, [
                      RoleService.get_or_create_role(RolesEnum.STUDENT, db)])
    db.add(user2)
    db.commit()

    # give access to user
    access = UserAccessPostModel(user=user2, post=postCreated)
    db.add(access)
    db.commit()

    postWithAccess = PostRepository.get_post_with_access(
        current_user_id=user2.id, post_id=postCreated.id, db=db)

    assert postCreated == postWithAccess


def test_get_post_without_access(db: Session, current_active_user: UserModel):
    # create posts
    title = "title"
    description = "askljdhf"

    postCreated = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)
    postCreated2 = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)

    # create user
    user2 = UserModel("lisa", "lasdhf", 23, False, [
                      RoleService.get_or_create_role(RolesEnum.STUDENT, db)])
    db.add(user2)
    db.commit()

    # give access to user
    access = UserAccessPostModel(user=user2, post=postCreated)
    db.add(access)
    db.commit()

    postWithAccess = PostRepository.get_post_with_access(
        current_user_id=user2.id, post_id=postCreated2.id, db=db)

    assert postWithAccess == None


def test_get_posts_with_access(db: Session, current_active_user: UserModel):
    # create users
    user2 = UserModel("lisa", "lasdhf", 23, False, [
                      RoleService.get_or_create_role(RolesEnum.STUDENT, db)])
    user3 = UserModel("asdf", "lasdasdfasdfhf", 24, False, [
                      RoleService.get_or_create_role(RolesEnum.TEACHING_ASSISTANT, db)])
    db.add_all([user2, user3])
    db.commit()

    # create posts
    title = "title"
    description = "askljdhf"

    postCreated = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)
    postCreated2 = PostService.create_post_for_user(
        title=title, description=description, user=current_active_user, db=db)
    postCreated3 = PostService.create_post_for_user(
        title=title, description=description, user=user3, db=db)

    db.add_all([postCreated, postCreated2, postCreated3])
    db.commit()

    # give access to user
    access1 = UserAccessPostModel(user=user2, post=postCreated)
    access2 = UserAccessPostModel(user=user2, post=postCreated2)
    access3 = UserAccessPostModel(user=user2, post=postCreated3)
    db.add_all([access1, access2, access3])
    db.commit()

    # request posts from current_active_user as user2
    postsWithAccess = PostRepository.get_posts_with_access(
        current_user_id=user2.id, user_id=current_active_user.id, db=db)
    assert len(postsWithAccess) == 2
    assert postCreated in postsWithAccess
    assert postCreated2 in postsWithAccess
    assert postCreated3 not in postsWithAccess
