"""Definitions of SQLAlchemy table-backed object mappings called entities."""


from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Self
from models import Role


class Base(DeclarativeBase):
    pass

# TODO: Create an entity for User data (Audrey)

# TODO: Create an entity for Organization data (Brianna)

# TODO: Create an entity for Events data (Brianna)

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

