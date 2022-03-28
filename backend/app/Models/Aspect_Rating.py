from database import Base
from sqlalchemy import Table, Column, ForeignKey

Aspect_Rating_Model = Table('aspect_rating', Base.metadata,
                            Column('aspect_id', ForeignKey('aspect.id')),
                            Column('rating_id', ForeignKey('rating.id'))
                            )
