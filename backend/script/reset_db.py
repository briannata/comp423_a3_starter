import database
from entities import Base, RegistrationEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# TODO: Reset the database.

""" Reset database """

registration = RegistrationEntity(id=0, user_id=0, event_id=0, status = 0)
session.add(registration)
session.commit()

# user = UserEntity(pid=730489388, first_name="Brianna", last_name="Ta")
# session.add(user)
# session.commit()