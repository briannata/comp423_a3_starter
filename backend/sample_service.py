from fastapi import Depends
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy.orm import Session
from database import db_session
from models import User
from entities import UserEntity


# TODO: Create separate service file called `user_service` for User data (Audrey)

# TODO: Create separate service file called `organization_service` for Organization data (Brianna)

# TODO: Create separate service file called `events_service` for Events data (Brianna)

# TODO: Create separate service file called `roles_service` for Roles data (Ajay)

# TODO: Create separate service file called `registrations_service` for Registrations data (Jade)


""" This is a sample service """

# class SampleService:

#     _session: Session

#     def __init__(self, session: Session = Depends(db_session)):
#         self._session = session

#     def all(self) -> list[User]:
#         query = select(UserEntity)
#         entities = self._session.scalars(query).all()
#         return [entity.to_model() for entity in entities]

#     def create(self, user: User) -> User:
#         if self._session.get(UserEntity, user.pid):
#             raise ValueError(f"Duplicate user found with PID: {user.pid}")
#         else:
#             user_entity = UserEntity.from_model(user)
#             self._session.add(user_entity)
#             self._session.commit()
#             return user_entity.to_model()

#     def get(self, pid: int) -> User | None:
#         user = self._session.get(UserEntity, pid)
#         if user:
#             return user.to_model()
#         else:
#             raise Exception(f"No user found with PID: {pid}")

#     def delete(self, pid: int) -> None:
#         obj=self._session.query(UserEntity).filter(UserEntity.pid==pid).first()
#         if obj:
#             self._session.delete(obj)
#             self._session.commit()
#         else:
#             raise Exception(f"No user found with PID: {pid}")