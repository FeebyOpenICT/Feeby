from .Rating import Base
from sqlalchemy import Table, Column, ForeignKey

aspect_rating = Table('aspect_rating', Base.metadata,
                      Column('aspect_id', ForeignKey('aspect.id')),
                      Column('rating_id', ForeignKey('rating.id'))
                      )