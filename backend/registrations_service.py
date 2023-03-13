from fastapi import Depends
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy.orm import Session
from database import db_session
from models import Registration, User, Event
from entities import RegistrationEntity

""" This is a sample service """

class RegistrationsService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Registration]:
        query = select(RegistrationEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def create(self, registration: Registration) -> Registration:
      # Attempt to get RegistrationEntity based on the IDs of the given user and event.
      registration = self._session.query(RegistrationEntity).filter(
        RegistrationEntity.user_id == registration.user_id, 
        RegistrationEntity.event_id == registration.event_id).one()
      # potentially put this in try catch in case one raises exception! (duplicate regs)

      # Check if the registration already exists in the table.
      if registration:
        # If the registration exists, raise a value error with a description.
        raise ValueError(f"{registration.user_id.first_name} {registration.user_id.last_name} is already registered for the event '{registration.event_id.name}'.")
      else:
        # If the registration does not exist, create a new registration.
        registration_entity = RegistrationEntity.from_model(registration)
        self._session.add(registration_entity)
        self._session.commit()
        return registration_entity.to_model()
      
    def get_by_user(self, user_id: int, status: int) -> list[Registration]:
       user = self._session.get(UserEntity, user_id)
       
       if user:
          entities = self._session.query(RegistrationEntity).filter(
             RegistrationEntity.user_id == user_id)
          return [entity.to_model() for entity in entities]
       else:
          raise ValueError(f"The user with the ID {user_id} does not exist.")
        
    # def get(self, pid: int) -> User | None:
    #     user = self._session.get(UserEntity, pid)
    #     if user:
    #         return user.to_model()
    #     else:
    #         raise Exception(f"No user found with PID: {pid}")

    # def delete(self, pid: int) -> None:
    #     obj=self._session.query(UserEntity).filter(UserEntity.pid==pid).first()
    #     if obj:
    #         self._session.delete(obj)
    #         self._session.commit()
    #     else:
    #         raise Exception(f"No user found with PID: {pid}")