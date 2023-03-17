from fastapi import FastAPI, Depends, HTTPException
from user_service import UserService, User
from role_service import RoleService, Role

app = FastAPI()


# TODO: Create API routes for User data (Audrey)

@app.get("/api/users")
def get_users(user_service: UserService = Depends()) -> list[User]:
    """
    Get all users

    Returns:
        list[User]: All `User`s in the `User` database table
    """

    # Return all roles
    return user_service.all()

@app.post("/api/users")
def new_user(user: User, user_service: UserService = Depends()) -> User:
    """
    Create or update user

    Returns:
        User: Latest iteration of the created or updated user after changes made
    """

    # Try to create / update user
    try:
        # Return created / updated user
        return user_service.create(user)
    except Exception as e:
        # Raise 422 exception if creation fails
        # - This would occur if the request body is shaped incorrectly
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/users/{pid}", responses={404: {"model": None}})
def get_user(pid: int, user_service: UserService = Depends()) -> User:
    """
    Get user with matching pid

    Returns:
        User: User with matching pid
    """
    
    # Try to get user with matching pid
    try: 
        # Return user
        return user_service.get_from_userpid(pid)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/users/{pid}")
def delete_role(pid: int, user_service = Depends(UserService)):
    """
    Delete user based on pid
    """

    # Try to delete user
    try:
        # Return deleted role
        return user_service.delete(pid)
    except Exception as e:
        # Raise 404 exception if search fails
        # - This would occur if there is no response or if item to delete does not exist
        raise HTTPException(status_code=404, detail=str(e))

# TODO: Create API routes for Organization data (Brianna)

# TODO: Create API routes for Events data (Brianna)

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