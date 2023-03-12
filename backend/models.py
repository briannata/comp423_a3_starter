from pydantic import BaseModel

# TODO: Create database models for User data (Audrey)

# TODO: Create database models for Organization data (Brianna)

# TODO: Create database models for Events data (Brianna)

# TODO: Create database models for Roles data (Ajay)
class Role(BaseModel):
    id: int
    user_id: int
    org_id: int
    membership_type: int

# TODO: Create database models for Registrations data (Jade)

""" Sample models """

# class User(BaseModel):
#     pid: int 
#     first_name: str
#     last_name: str
