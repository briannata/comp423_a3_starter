"""Definitions of SQLAlchemy table-backed object mappings called entities."""


from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Self
from models import Role, Organization, Event

from datetime import datetime


class Base(DeclarativeBase):
    pass

# TODO: Create an entity for User data (Audrey)

# TODO: Create an entity for Organization data (Brianna)
class OrganizationEntity(Base):
    """Serves as the database model schema defining the shape of the `Organization` table"""

    __tablename__ = "organization"

    # Unique ID for the organization
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Name of the organization
    name: Mapped[str] = mapped_column(String)
    # Logo of the organization
    logo: Mapped[str] = mapped_column(String)
    # Short description of the organization
    short_description: Mapped[str] = mapped_column(String)
    # Long description of the organization
    long_description: Mapped[str] = mapped_column(String)
    # Website of the organization
    website: Mapped[str] = mapped_column(String)
    # Contact email for the organization
    email: Mapped[str] = mapped_column(String)
    # Instagram username for the organization
    instagram: Mapped[str] = mapped_column(String)
    # LinkedIn for the organization
    linked_in: Mapped[str] = mapped_column(String)
    # YouTube for the organization
    youtube: Mapped[str] = mapped_column(String)
    # Heel Life for the organization
    heel_life: Mapped[str] = mapped_column(String)

    @classmethod
    def from_model(cls, model: Organization) -> Self:
        """
        Class method that converts a `Organization` object into a `OrganizationEntity`
        
        Parameters:
            - model (Organization): Model to convert into an entity

        Returns:
            OrganizationEntity: Entity created from model
        """
        return cls(id=model.id, name=model.name, logo=model.logo, short_description=model.short_description, long_description=model.long_description, website=model.website, email=model.email, instagram=model.instagram, linked_in=model.linked_in, youtube=model.youtube, heel_life=model.heel_life)

    def to_model(self) -> Organization:
        """
        Converts a `OrganizationEntity` object into a `Organization`
        
        Returns:
            Organization: `Organization` object from the entity
        """
        return Organization(id=self.id, name=self.name, logo=self.logo, short_description=self.short_description, long_description=self.long_description, website=self.website, email=self.email, instagram=self.instagram, linked_in=self.linked_in, youtube=self.youtube, heel_life=self.heel_life)

# TODO: Create an entity for Events data (Brianna)
class EventEntity(Base):
    """Serves as the database model schema defining the shape of the `Event` table"""

    __tablename__ = "event"

    # Unique ID for the event
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Name of the event
    name: Mapped[str] = mapped_column(String)
    # Time of the event
    time: Mapped[datetime] = mapped_column(DateTime)
    # Location of the event
    location: Mapped[str] = mapped_column(String)
    # Description of the event
    description: Mapped[str] = mapped_column(String)
    # Whether the event is public or not
    public: Mapped[bool] = mapped_column(Boolean)
    # ID of the organization hosting the event
    org_id: Mapped[int] = mapped_column(Integer)

    @classmethod
    def from_model(cls, model: Event) -> Self:
        """
        Class method that converts a `Event` object into a `EventEntity`
        
        Parameters:
            - model (Event): Model to convert into an entity

        Returns:
            EventEntity: Entity created from model
        """
        return cls(id=model.id, name=model.name, time=model.time, location=model.location, description=model.description, public=model.public, org_id=model.org_id)

    def to_model(self) -> Event:
        """
        Converts a `EventEntity` object into a `Event`
        
        Returns:
            Event: `Event` object from the entity
        """
        return Event(id=self.id, name=self.name, time=self.time, location=self.location, description=self.description, public=self.public, org_id=self.org_id)


# TODO: Create an entity for Roles data (Ajay)
class RoleEntity(Base):
    """Serves as the database model schema defining the shape of the `Role` table"""

    __tablename__ = "role"

    # Unique ID for the role
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # User ID for the role
    user_id: Mapped[int] = mapped_column(Integer)
    # Organization ID for the role
    org_id: Mapped[int] = mapped_column(Integer)
    # Type of membership (0 = Member, 1 = Executive, 3 = Owner)
    membership_type: Mapped[int] = mapped_column(Integer)

    @classmethod
    def from_model(cls, model: Role) -> Self:
        """
        Class method that converts a `Role` object into a `RoleEntity`
        
        Parameters:
            - model (Role): Model to convert into an entity

        Returns:
            RoleEntity: Entity created from model
        """
        return cls(id=model.id, user_id=model.user_id, org_id=model.org_id, membership_type=model.membership_type)

    def to_model(self) -> Role:
        """
        Converts a `RoleEntity` object into a `Role`
        
        Returns:
            Role: `Role` object from the entity
        """
        return Role(id=self.id, user_id=self.user_id, org_id=self.org_id, membership_type=self.membership_type)

# TODO: Create an entity for Registrations data (Jade)



""" This is a sample entity """

# class UserEntity(Base):
#     __tablename__ = "users"

#     pid: Mapped[int] = mapped_column(Integer, primary_key=True)
#     first_name: Mapped[str] = mapped_column(String(64))
#     last_name: Mapped[str] = mapped_column(String(64))

#     @classmethod
#     def from_model(cls, model: User) -> Self:
#         return cls(pid=model.pid, first_name=model.first_name, last_name=model.last_name)

#     def to_model(self) -> User:
#         return User(pid=self.pid, first_name=self.first_name, last_name=self.last_name)

