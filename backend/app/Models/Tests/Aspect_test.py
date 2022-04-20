import pytest
from sqlalchemy.orm import Session
from Models.AspectModel import AspectModel

from Models.RatingModel import RatingModel


def test_create_aspect_with_positional_arguments(db: Session):
    rating = RatingModel('title', 'short_desc', 'desc')
    db.add(rating)
    db.commit()

    aspect = AspectModel('title', 'short_desc', 'desc', 'ext_url', [rating])
    db.add(aspect)
    db.commit()

    assert aspect.id == 1
    assert aspect.title == 'title'
    assert aspect.description == 'desc'
    assert aspect.short_description == 'short_desc'
    assert len(aspect.ratings) == 1
    assert aspect.ratings[0].id == rating.id
    assert aspect.ratings[0].title == rating.title
    assert aspect.ratings[0].description == rating.description
    assert aspect.ratings[0].short_description == rating.short_description


def test_create_aspect_without_ratings(db: Session):
    with pytest.raises(ValueError):
        aspect = AspectModel('title', 'short_desc', 'desc', 'ext_url', [])
