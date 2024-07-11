from sqlalchemy import Column, Integer, String, Boolean, MetaData, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

# Create a MetaData instance
metadata = MetaData()

# Create a Base class using the declarative base
Base = declarative_base()

# Define the 'roles' table
roles_table = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),  # Primary key, auto-incremented
    Column('name', String(255), nullable=False),  # Role name, not nullable
    Column('permission', String(255), nullable=False)  # Permission, not nullable
)

# Define the 'regions' table
regions_table = Table(
    'regions',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),  # Primary key, auto-incremented
    Column('region_name', String(255), nullable=False),  # Region name, not nullable
    Column('parent_id', Integer, ForeignKey('regions.id'), nullable=True)  # Self-referential foreign key, nullable
)

# Define the 'users' table
users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),  # Primary key, auto-incremented
    Column('role_id', Integer, ForeignKey('roles.id')),  # Foreign key to 'roles' table
    Column('first_name', String(255), nullable=False),  # First name, not nullable
    Column('second_name', String(255), nullable=False),  # Second name, not nullable
    Column('last_name', String(255), nullable=False),  # Last name, not nullable
    Column('born', String(255), nullable=False),  # Date of birth, not nullable
    Column('phone_number', String(255), nullable=False),  # Phone number, not nullable
    Column('email', String(255), nullable=False),  # Email, not nullable
    Column('sex', String(255), nullable=False),  # Sex, not nullable
    Column('country_id', Integer, ForeignKey('regions.id')),  # Foreign key to 'regions' table for country
    Column('city_id', Integer, ForeignKey('regions.id')),  # Foreign key to 'regions' table for city
    Column('street_id', Integer, ForeignKey('regions.id')),  # Foreign key to 'regions' table for street
    Column('avatar', String(255), nullable=False),  # Avatar URL, not nullable
    Column('description', String(255), nullable=False),  # Description, not nullable
)

# Define the Role class mapped to the 'roles' table
class Role(Base):
    __table__ = roles_table

    id = roles_table.c.id
    name = roles_table.c.name
    permission = roles_table.c.permission

    # Optional relationship to User
    users = relationship('User', backref='role')

# Define the Region class mapped to the 'regions' table
class Region(Base):
    __table__ = regions_table

    id = regions_table.c.id
    region_name = regions_table.c.region_name
    parent_id = regions_table.c.parent_id

    # Relationship to self for hierarchical regions
    subregions = relationship('Region', backref='parent', remote_side=[id]) 

# Define the User class mapped to the 'users' table
class User(Base):
    __table__ = users_table

    id = users_table.c.id
    role_id = users_table.c.role_id
    first_name = users_table.c.first_name
    second_name = users_table.c.second_name
    last_name = users_table.c.last_name 
    born = users_table.c.born
    phone_number = users_table.c.phone_number
    email = users_table.c.email
    sex = users_table.c.sex
    country_id = users_table.c.country_id
    city_id = users_table.c.city_id
    street_id = users_table.c.street_id
    avatar = users_table.c.avatar
    description = users_table.c.description

    # Relationships to other tables
    role = relationship(Role)  # Relationship to Role object
    country = relationship('Region', foreign_keys=[country_id])  # Relationship to Region as country
    city = relationship('Region', foreign_keys=[city_id])  # Relationship to Region as city
    street = relationship('Region', foreign_keys=[street_id])  # Relationship to Region as street