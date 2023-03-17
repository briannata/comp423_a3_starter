from fastapi import FastAPI, Depends, HTTPException
from registrations_service import RegistrationsService, Registration

app = FastAPI()


# TODO: Create API routes for User data (Audrey)

# TODO: Create API routes for Organization data (Brianna)

# TODO: Create API routes for Events data (Brianna)

# TODO: Create API routes for Roles data (Ajay)

# TODO: Create API routes for Registrations data (Jade)
@app.get("/api/registrations")
def get_registrations(registrations_service: RegistrationsService = Depends()) -> list[Registration]:
  """
  Get all registrations for all events.

  Args:
    registration_service is a valid RegistrationService.

  Returns:
    list[Role]: All `Registration`s in the `Registrations` database table
  """
  return registrations_service.all()

@app.post("/api/registrations")
def create_registration(registration: Registration, registrations_service: RegistrationsService = Depends()) -> Registration:
  """
  Create a registration by a user for an event.

  Args:
    registration is a valid Registration model.
    registration_service is a valid RegistrationService.

  Returns:
    The Registration object for the user.

  Raises:
    HTTPException 422 if create() raises an Exception.
  """
  try:
    return registrations_service.create(registration)
  except Exception as e:
    raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/registrations/{user_id}/{status}")
def get_registrations_by_user(user_id: int, status: int, registrations_service: RegistrationsService = Depends()) -> list[Registration]:
  """
  Get all Registration objects associated with a User based on attendance status.

  Args:
    user_id is an Integer representing a unique identifier for a user.
    status is an Integer representing if the user has registered for (0) or attended (1) an event.
    registration_service is a valid RegistrationService.

  Returns:
    list of Events the user has registered for or attended.

  Raises:
    HTTPException 422 if get_by_user() raises an Exception.
  """
  try:
    return registrations_service.get_by_user(user_id, status)
  except Exception as e:
    raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/registrations/{event_id}/{status}")
def get_registrations_by_event(event_id: int, status: int, registrations_service: RegistrationsService = Depends()) -> list[Registration]:
  """
  Get all registrations associated with an Event based on attendance status.

  Args:
    event_id is an Integer representing a unique identifier for an event.
    status is an Integer representing if the user has registered for (0) or attended (1) an event.
    registration_service is a valid RegistrationService.

  Returns:
    list of Users who are registered for or attended the event.

  Raises:
    HTTPException 422 if get_by_event() raises an Exception.
  """
  try:
    return registrations_service.get_by_event(event_id, status)
  except Exception as e:
    raise HTTPException(status_code=422, detail=str(e))

@app.put("/api/registrations/{user_id}/{event_id}")
def mark_attended(registration: Registration, registrations_service: RegistrationsService = Depends()) -> Registration:
  """
  Update a User's attendance status for an Event.

  Args:
    registration is a valid Registration model.
    registration_service is a valid RegistrationService.

  Returns:
    The updated Registration object

  Raises:
    HTTPException 422 if update_status() raises an Exception.
  """
  try:
    return registrations_service.update_status(registration)
  except Exception as e:
    raise HTTPException(status_code=422, detail=str(e))

@app.delete("/api/registrations/{user_id}/{event_id}")
def delete_registration(registration: Registration, registrations_service: RegistrationsService = Depends()) -> None:
  """
  Delete Registration for Event based on the User and the Event.

  Args:
    registration is a valid Registration model.
    registration_service is a valid RegistrationService.

  Returns:
    None

  Raises:
    HTTPException 404 if delete_registration() raises an Exception.
  """
  try:
    registrations_service.delete_registration(registration)
  except Exception as e:
    raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/registrations/{event_id}")
def clear_event_registrations(event_id: int, registrations_service: RegistrationsService = Depends()) -> None:
  """
  Clear all registrations for an event.

  Args:
    event_id is an Integer representing a unique identifier for an event.
    registration_service is a valid RegistrationService.

  Returns:
    None

  Raises:
    HTTPException 404 if clear_registrations() raises an Exception.
  """

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