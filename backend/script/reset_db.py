import database
from entities import Base, UserEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# TODO: Reset the database.

""" Reset database """

# user = UserEntity(pid=730489388, first_name="Brianna", last_name="Ta")
# session.add(user)
# session.commit()