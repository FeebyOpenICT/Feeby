import pytest

from sqlalchemy.orm import Session

from Models.PostModel import PostModel


def test_initiate_post_without_user():
    with pytest.raises(TypeError):
        post = PostModel("kajshdf", "kajhsdf")


def test_create_post_with_positional_arguments(db: Session, current_active_user):
    post = PostModel('title', 'desc', current_active_user)
    post.save_self(db)

    assert post.title == 'title'
    assert post.description == 'desc'
    assert post.id == 1
    assert post.user == current_active_user
    assert post.time_created is not None
    assert post.time_updated is not None
