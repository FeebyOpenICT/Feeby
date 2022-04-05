from database import Base
from sqlalchemy import Table, Column, ForeignKey


UserRoleModel = Table('user_role', Base.metadata,
                      Column('user_id', ForeignKey('user.id')),
                      Column('role_id', ForeignKey('role.id')),
                      extend_existing=True,
                      )
