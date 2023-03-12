"""Definitions of SQLAlchemy table-backed object mappings called entities."""


from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Self
from models import User
from models import Registration


class Base(DeclarativeBase):
    pass

# TODO: Create an entity for User data (Audrey)

# TODO: Create an entity for Organization data (Brianna)

# TODO: Create an entity for Events data (Brianna)

# TODO: Create an entity for Roles data (Ajay)

# TODO: Create an entity for Registrations data (Jade)
class RegistrationEntity(Base):
    """Serves as the database model schema defining the shape of the `Registrations` table."""
    
    __tablename__ = "registrations"

    # Unique ID for a registration
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # User ID associated with registration
    user_id: Mapped[int] = mapped_column(Integer)
    # Event ID associated with registration
    event_id: Mapped[int] = mapped_column(Integer)
    # Status of Registration (0 = Registered, 1 = Registered + Attended)
    status: Mapped[int] = mapped_column(Integer)

    @classmethod
    def from_model(cls, model: Registration) -> Self:
        """
        Class method that converts a `Registration` object into a `RegistrationEntity`
        
        Parameters:
            - model (Registration): Model to convert into an entity
        
        Returns:
            RegistrationEntity: Entity created from model
        """
        return cls(id=model.id, user_id=model.user_id, event_id=model.event_id, status=model.status)

    def to_model(self) -> User:
        """
        Class method that converts a `RegistrationEntity` into a `Registration` object
        
        Parameters: None
        
        Returns:
            Registration: `Registration` object from the entity
        """
        return Registration(id=self.id, user_id=self.user_id, event_id=self.event_id, status=self.status)


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

