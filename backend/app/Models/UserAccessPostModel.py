from database import Base
from sqlalchemy import Table, Column, ForeignKey


UserAccessPostModel = Table('user_access_post', Base.metadata,
                            Column('user_id', ForeignKey('user.id')),
                            Column('post_id', ForeignKey('post.id')),
                            extend_existing=True,
                            )
