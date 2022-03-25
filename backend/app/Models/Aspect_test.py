import pytest
from sqlalchemy.orm import Session
from Models.Aspect import AspectModel

from Models.Rating import RatingModel


def test_create_aspect_with_positional_arguments(db: Session):
    rating = RatingModel('title', 'short_desc', 'desc')
    rating.save_self(db)

    aspect = AspectModel('title', 'short_desc', 'desc', 'ext_url', [rating])
    aspect.save_self(db)

    assert aspect.id is not None
