from pydantic import BaseModel

# TODO: Create database models for User data (Audrey)

# TODO: Create database models for Organization data (Brianna)

# TODO: Create database models for Events data (Brianna)

# TODO: Create database models for Roles data (Ajay)

# TODO: Create database models for Registrations data (Jade)
class Registration(BaseModel):
  """
  Model to represent `Registration` connections between users and organizations
    
  This model is based on the `RegistrationEntity` model, which defines the shape
  of the `Registrations` database in the PostgreSQL database
  """
    
  user_id: int
  event_id: int
  status: int

""" Sample models """

# class User(BaseModel):
#     pid: int 
#     first_name: str
#     last_name: str
