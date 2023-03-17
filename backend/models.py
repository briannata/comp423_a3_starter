from pydantic import BaseModel
from sqlalchemy import Date

# TODO: Create database models for User data (Audrey)
class User(BaseModel):
    """
    Model to represent a `User` on the CSXL website
    
    This model is based on the `UserEntity` entity, which defines the shape
    of the `User` database in the PostgreSQL database
    """
    
    pid: int
    first_name: str
    last_name: str
    email: str
    user_type: int
    graduation_date: Date
    major1: str
    major2: str
    minor1: str
    minor2: str

# TODO: Create database models for Organization data (Brianna)

# TODO: Create database models for Events data (Brianna)

# TODO: Create database models for Roles data (Ajay)

class Role(BaseModel):
    """
    Model to represent `Role` connections between users and organizations
    
    This model is based on the `RoleEntity` model, which defines the shape
    of the `Role` database in the PostgreSQL database
    """
    
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
