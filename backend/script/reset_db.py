import database
from entities import Base, UserEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# TODO: Add a UserEntity to the database session and commit it.
user = UserEntity(pid=730489388, first_name="Brianna", last_name="Ta")
session.commit()