from fastapi import FastAPI, Depends, HTTPException
from role_service import RoleService, Role

app = FastAPI()


# TODO: Create API routes for User data (Audrey)

# TODO: Create API routes for Organization data (Brianna)

# TODO: Create API routes for Events data (Brianna)

# TODO: Create API routes for Roles data (Ajay)
@app.get("/api/roles")
def get_roles(role_service: RoleService = Depends()) -> list[Role]:
    return role_service.all()

@app.post("/api/roles")
def new_role(role: Role, role_service: RoleService = Depends()) -> Role:
    try:
        return role_service.create(role)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/api/roles/user/{user_id}", responses={404: {"model": None}})
def get_role_from_userid(user_id: int, role_service: RoleService = Depends()) -> list[Role]:
    try: 
        return role_service.get_from_userid(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/roles/org/{org_id}", responses={404: {"model": None}})
def get_role_from_userid(org_id: int, role_service: RoleService = Depends()) -> list[Role]:
    try: 
        return role_service.get_from_orgid(org_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/roles/{id}")
def delete_role(id: int, role_service = Depends(RoleService)):
    try: 
        return role_service.delete(id)
    except Exception as e:
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