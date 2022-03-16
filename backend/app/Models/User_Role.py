from .Role import Base
from sqlalchemy import Table, Column, ForeignKey


user_role = Table('user_role', Base.metadata,
  Column('user_id', ForeignKey('user.id'), primary_key=True),
  Column('role_id', ForeignKey('role.id'), primary_key=True)
)
