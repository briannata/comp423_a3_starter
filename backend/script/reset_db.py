import database
from entities import Base, RoleEntity

# Reset Tables
Base.metadata.drop_all(database.engine)
Base.metadata.create_all(database.engine)

# Enter Mock Data
from sqlalchemy.orm import Session
session = Session(database.engine)

# TODO: Reset the database.
role = RoleEntity(id=1, user_id=1, org_id=1, membership_type = 1)
session.add(role)
session.commit()

""" Reset database """

# user = UserEntity(pid=730489388, first_name="Brianna", last_name="Ta")
# session.add(user)
# session.commit()