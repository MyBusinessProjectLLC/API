from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

metadata = MetaData()

Base = declarative_base()

roles_table = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
    Column('permission', String(255), nullable=False)
)

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('role_id', Integer, ForeignKey('roles.id')),
    Column('name', String(255), nullable=False)
)


class Role(Base):
    __table__ = roles_table

    id = roles_table.c.id
    name = roles_table.c.name
    permission = roles_table.c.permission

    # Consider adding a relationship to User if required for your use case
    users = relationship('User', backref='role')  # Optional relationship


class User(Base):
    __table__ = users_table

    id = users_table.c.id
    role_id = users_table.c.role_id
    name = users_table.c.name

    role = relationship(Role)  # Relationship to Role object
