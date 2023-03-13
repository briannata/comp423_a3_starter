from fastapi import FastAPI, Depends, HTTPException
from registrations_service import RegistrationsService, Registration

app = FastAPI()


# TODO: Create API routes for User data (Audrey)

# TODO: Create API routes for Organization data (Brianna)

# TODO: Create API routes for Events data (Brianna)

# TODO: Create API routes for Roles data (Ajay)

# TODO: Create API routes for Registrations data (Jade)
@app.get("/api/registrations")
def get_registrations():
  """Get all registrations for all events."""
  # TODO
  return

@app.post("/api/registrations")
def create_registration(registration: Registration, registrations_service: RegistrationsService = Depends()) -> Registration:
  """Create a registration by a user for an event."""
  try:
    return registrations_service.create(registration)
  except Exception as e:
    raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/registrations/{user_id}/{status}")
def get_registrations_by_user(user_id: int, status: int, registrations_service: RegistrationsService = Depends()) -> list[Registration]:
  """Get a user's registered and/or attended events."""
  try:
    return registrations_service.get_by_user(user_id, status)
  except Exception as e:
    raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/registrations/{event_id}/{status}")
def get_registrations_by_event(event_id: int, status: int, registrations_service: RegistrationsService = Depends()) -> list[Registration]:
  """Get an event's registered or attended users."""
  try:
    return registrations_service.get_by_event(event_id, status)
  except Exception as e:
    raise HTTPException(status_code=422, detail=str(e))

@app.delete("/api/registrations/{user_id}/{event_id}")
def delete_registration(user_id: int, event_id: int, registrations_service: RegistrationsService = Depends()) -> None:
  """Delete registration for an event based on the user and the event."""
  try:
    registrations_service.delete_registration(user_id, event_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/registrations/{event_id}")
def clear_event_registrations(event_id: int, registrations_service: RegistrationsService = Depends()) -> None:
  """Clear all registrations for an event."""
  try:
    registrations_service.clear_registrations(event_id)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))


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