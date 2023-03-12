from fastapi import FastAPI, Depends, HTTPException
from user_service import UserService, User

app = FastAPI()


# TODO: Create API routes for User data (Audrey)

# TODO: Create API routes for Organization data (Brianna)

# TODO: Create API routes for Events data (Brianna)

# TODO: Create API routes for Roles data (Ajay)

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