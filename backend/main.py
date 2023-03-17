from fastapi import FastAPI, Depends, HTTPException
from role_service import RoleService, Role
from organization_service import OrganizationService, Organization
from event_service import EventService, Event
from datetime import datetime

app = FastAPI()


# TODO: Create API routes for User data (Audrey)

# TODO: Create API routes for Organization data (Brianna)
@app.get("/api/organizations")
def get_organizations(organization_service: OrganizationService = Depends()) -> list[Organization]:
    """
    Get all organizations

    Returns:
        list[Organization]: All `Organizations`s in the `Organization` database table
    """

    # Return all organizations
    return organization_service.all()

@app.post("/api/organizations")
def new_organization(organization: Organization, organization_service: OrganizationService = Depends()) -> Organization:
    """
    Create or update organization

    Returns:
        Organization: Latest iteration of the created or updated organization after changes made
    """

    # Try to create / update organization
    try:
        # Return created / updated organization
        return organization_service.create(organization)
    except Exception as e:
        # Raise 422 exception if creation fails
        # - This would occur if the request body is shaped incorrectly
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/organizations/{id}", responses={404: {"model": None}})
def get_organization_from_id(id: int, organization_service: OrganizationService = Depends()) -> Organization:
    """
    Get organization with matching id

    Returns:
        Organization: Organization with matching id
    """
    
    # Try to get organization with matching id
    try: 
        # Return organization
        return organization_service.get_from_id(id)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/api/organizations/", responses={404: {"model": None}})
def update_organization(organization: Organization, organization_service: OrganizationService = Depends()) -> Organization:
    """
    Update organization

    Returns:
        Organization: Updated organization
    """

    # Try to update organization
    try: 
        # Return updated organization
        return organization_service.update(organization)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/organizations/{id}")
def delete_organization(id: int, organization_service = Depends(OrganizationService)):
    """
    Delete organization based on id
    """

    # Try to delete organization
    try:
        # Return deleted organization
        return organization_service.delete(id)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response or if item to delete does not exist
        raise HTTPException(status_code=404, detail=str(e))

# TODO: Create API routes for Events data (Brianna)
@app.get("/api/events")
def get_events(event_service: EventService = Depends()) -> list[Event]:
    """
    Get all events

    Returns:
        list[Event]: All `Event`s in the `Event` database table
    """

    # Return all events
    return event_service.all()

@app.get("/api/events/org/{id}")
def get_events_org_id(org_id: int, event_service: EventService = Depends()) -> list[Event]:
    """
    Get all events from an organization

    Returns:
        list[Event]: All `Event`s in the `Event` database table from a specific organization
    """

    # Return all events
    return event_service.get_from_org_id(org_id)

@app.get("/api/events/time/")
def get_events_from_time_range(start: datetime, end: datetime, event_service: EventService = Depends()) -> list[Event]:
    """
    Get all events from a time range

    Returns:
        list[Event]: All `Event`s in the `Event` database table in a specific time range
    """

    # Return all events
    return event_service.get_from_time_range(start, end)

@app.post("/api/events")
def new_event(event: Event, event_service: EventService = Depends()) -> Event:
    """
    Create or update event

    Returns:
        Event: Latest iteration of the created or updated event after changes made
    """

    # Try to create / update event
    try:
        # Return created / updated event
        return event_service.create(event)
    except Exception as e:
        # Raise 422 exception if creation fails
        # - This would occur if the request body is shaped incorrectly
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/events/{id}", responses={404: {"model": None}})
def get_event_from_id(id: int, event_service: EventService = Depends()) -> Event:
    """
    Get event with matching id

    Returns:
        Event: Event with matching id
    """
    
    # Try to get event with matching id
    try: 
        # Return event
        return event_service.get_from_id(id)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response
        raise HTTPException(status_code=404, detail=str(e))

@app.put("/api/events/", responses={404: {"model": None}})
def update_event(organization: Event, event_service: EventService = Depends()) -> Event:
    """
    Update event

    Returns:
        Event: Updated event
    """

    # Try to update event
    try: 
        # Return updated event
        return event_service.update(organization)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/events/{id}")
def delete_event(id: int, event_service = Depends(EventService)):
    """
    Delete event based on id
    """

    # Try to delete event
    try:
        # Return deleted event
        return event_service.delete(id)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response or if item to delete does not exist
        raise HTTPException(status_code=404, detail=str(e))

# TODO: Create API routes for Roles data (Ajay)

@app.get("/api/roles")
def get_roles(role_service: RoleService = Depends()) -> list[Role]:
    """
    Get all roles

    Returns:
        list[Role]: All `Role`s in the `Role` database table
    """

    # Return all roles
    return role_service.all()

@app.post("/api/roles")
def new_role(role: Role, role_service: RoleService = Depends()) -> Role:
    """
    Create or update role

    Returns:
        Role: Latest iteration of the created or updated role after changes made
    """

    # Try to create / update role
    try:
        # Return created / updated role
        return role_service.create(role)
    except Exception as e:
        # Raise 422 exception if creation fails
        # - This would occur if the request body is shaped incorrectly
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/roles/user/{user_id}", responses={404: {"model": None}})
def get_role_from_userid(user_id: int, role_service: RoleService = Depends()) -> list[Role]:
    """
    Get all roles with matching user_id

    Returns:
        list[Role]: All roles with matching user_id
    """
    
    # Try to get all roles with matching user_id
    try: 
        # Return roles
        return role_service.get_from_userid(user_id)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/roles/org/{org_id}", responses={404: {"model": None}})
def get_role_from_userid(org_id: int, role_service: RoleService = Depends()) -> list[Role]:
    """
    Get all roles with matching org_id

    Returns:
        list[Role]: All roles with matching org_id
    """

    # Try to get all roles with matching org_id
    try: 
        # Return roles
        return role_service.get_from_orgid(org_id)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/roles/{id}")
def delete_role(id: int, role_service = Depends(RoleService)):
    """
    Delete role based on id
    """

    # Try to delete role
    try:
        # Return deleted role
        return role_service.delete(id)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response or if item to delete does not exist
        raise HTTPException(status_code=404, detail=str(e))

# TODO: Create API routes for Registrations data (Jade)

""" These are sample routes """

# @app.get("/api/users")
# def get_users(user_service: UserService = Depends()) -> list[User]:
#     return user_service.all()


# @app.post("/api/users")
# def new_user(user: User, user_service: UserService = Depends()) -> User:
#     if len(str(user.pid)) != 9: raise HTTPException(status_code=422, detail=str("PID is not 9 digits"))
#     try:
#         return user_service.create(user)
#     except Exception as e:
#         raise HTTPException(status_code=422, detail=str(e))

# @app.get("/api/users/{pid}", responses={404: {"model": None}})
# def get_user(pid: int, user_service: UserService = Depends()) -> User:
#     try: 
#         return user_service.get(pid)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))


# @app.delete("/api/users/{pid}")
# def delete_user(pid: int, user_service = Depends(UserService)):
#     try: 
#         return user_service.delete(pid)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))