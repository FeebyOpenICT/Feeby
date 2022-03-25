# import pytest

# from sqlalchemy.orm import Session
# from .Rating import Rating
# from .Aspect import Aspect

# def test_create_aspect_with_positional_arguments(db: Session):
#     rating = Rating('title', 'short_desc', 'desc')
#     rating.save_self(db)

#     aspect = Aspect('title', 'short_desc', 'desc', 'ext_url', [rating])
#     aspect.save_self(db)

#     assert aspect.id is not None
