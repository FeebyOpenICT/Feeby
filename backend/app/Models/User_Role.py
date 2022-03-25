from database import Base
from sqlalchemy import Table, Column, ForeignKey


User_Role_Model = Table('user_role', Base.metadata,
                        Column('user_id', ForeignKey('user.id')),
                        Column('role_id', ForeignKey('role.id')),
                        extend_existing=True,
                        )
