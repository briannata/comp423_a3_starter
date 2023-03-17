from fastapi import Depends
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from database import db_session
from models import User
from entities import UserEntity

class UserService:
    """Service that performs all of the actions on the `User` table"""

    # Current SQLAlchemy Session
    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        """Initializes the `UserService` session"""
        self._session = session

    def all(self) -> list[User]:
        """
        Retrieves all users from the table

        Returns:
            list[User]: List of all `Users`
        """
        # Select all entries in `User` table
        query = select(UserEntity)
        entities = self._session.scalars(query).all()

        # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def create(self, user: User) -> User:
        """
        Creates a user based on the input object and adds it to the table.
        If the user's PID is unique to the table, a new entry is added.
        If the user's PID already exists in the table, the existing entry is updated.

        Parameters:
            user (User): User to add to table
        Returns:
            User: Object added to table
        """

        # Checks if the user already exists in the table
        if self._session.get(UserEntity, user.pid):

            # If so, update existing entry
            user_entity = UserEntity.from_model(user)
            self._session.execute(
                update(UserEntity)
                .where(UserEntity.pid == user.pid)
                .values(
                    pid = user_entity.pid,
                    first_name = user_entity.first_name,
                    last_name = user_entity.last_name,
                    email=user_entity.email,
                    membership_type=user_entity.membership_type,
                    graduation_date=user_entity.graduation_date,
                    major1=user_entity.major1,
                    major2=user_entity.major2,
                    minor1=user_entity.minor1,
                    minor2=user_entity.minor2
            ))

            # Commit changes
            self._session.commit()

            # Return updated object
            return user_entity.to_model()
        else:
            # Otherwise, create new object
            user_entity = UserEntity.from_model(user)

            # Add new object to table and commit changes
            self._session.add(user_entity)
            self._session.commit()

            # Return added object
            return user_entity.to_model()

    def get(self, pid: int) -> User:
        """
        Get user matching the provided user pid.
        If none retrieved, a debug description is displayed.

        Parameters:
            pid (int): Unique user PID
        Returns:
            User: Matching `User` object
        """

        # Get user with matching user id
        user = self._session.get(UserEntity, pid)

        # Check if result is null
        if user:
            # Convert entry to a model and return
            return user.to_model()
        else:
            #Raise exception
            raise Exception(f"No user found with PID: {pid}")

    def delete(self, pid: int) -> None:
        """
        Delete the user based on the provided PID.
        If no item exists to delete, a debug description is displayed.

        Parameters:
            pid (int): Unique user PID
        """

        # Find user to delete
        user=self._session.query(UserEntity).filter(UserEntity.pid == pid).first()

        # Ensure object exists
        if user:
            # Delete object and commit
            self._session.delete(user)
            self._session.commit()
        else:
            # Raise exception
            raise Exception(f"No user found with PID: {pid}")