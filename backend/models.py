from pydantic import BaseModel

# TODO: Create database models for User data (Audrey)

# TODO: Create database models for Organization data (Brianna)
class Organization(BaseModel):
    """
    Model to represent an `Organization` object
    
    This model is based on the `OrganizationEntity` model, which defines the shape
    of the `Organization` database in the PostgreSQL database
    """
    
    id: int
    name: str
    logo: str
    short_description: str
    long_description: str
    website: str
    email: str
    instagram: str
    linked_in: str
    youtube: str
    heel_life: str

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
