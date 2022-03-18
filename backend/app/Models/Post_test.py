from pdb import post_mortem
from sqlalchemy.orm import Session
import pytest

from Models.Post import Post


def test_initiate_post_without_user(db: Session):
    with pytest.raises(TypeError):
        post = Post("kajshdf", "kajhsdf")
