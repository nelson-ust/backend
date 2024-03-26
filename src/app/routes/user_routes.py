
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from db.database import get_db
# from services.user_service import UserService
# from schemas.user_schema import UserCreate, UserUpdate, UserLogin, User
# from auth.security import create_access_token, get_current_user, get_password_hash

# router = APIRouter()
# # user_service = UserService()

# @router.post("/login")
# def login(user_login: UserLogin, db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     user = user_service.authenticate_user(user_login)
#     if not user:
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     access_token = create_access_token(data={"user_id": user.id})
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.post("/users/", response_model=User)
# def create_user(user: UserCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     return user_service.create_user(user, current_user)

# @router.put("/users/{user_id}", response_model=User)
# def update_user(user_id: int, user_data: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     return user_service.update_user(user_id, user_data, current_user)

# @router.delete("/users/{user_id}", response_model=User)
# def delete_user(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     return user_service.delete_user(user_id, current_user)

# @router.get("/users/", response_model=list[User])
# def get_all_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     return user_service.get_all_users(current_user)

# @router.get("/active-users/", response_model=list[User])
# def get_active_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     return user_service.get_active_users(current_user)

# @router.get("/inactive-users/", response_model=list[User])
# def get_inactive_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     return user_service.get_inactive_users(current_user)

# @router.put("/users/{user_id}/update-token/")
# def update_user_token(user_id: int, token: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     user_service=UserService(db)
#     return user_service.update_user_token(user_id, token)


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from services.user_service import UserService
from schemas.user_schema import UserCreate, UserUpdate, UserLogin, User
from auth.security import create_access_token, get_current_user

router = APIRouter()

@router.post("/login")
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        user = user_service.authenticate_user(user_login)
        if not user:
            raise HTTPException(status_code=401, detail="Incorrect username or password")
        access_token = create_access_token(data={"user_id": user.id})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.create_user(user, current_user)
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.update_user(user_id, user_data, current_user)
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.delete_user(user_id, current_user)
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/", response_model=list[User])
def get_all_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.get_all_users(current_user)
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/active-users/", response_model=list[User])
def get_active_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.get_active_users(current_user)
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/inactive-users/", response_model=list[User])
def get_inactive_users(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.get_inactive_users(current_user)
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/users/{user_id}/update-token/")
def update_user_token(user_id: int, token: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user_service = UserService(db)
        return user_service.update_user_token(user_id, token)
    except PermissionError as pe:
        raise HTTPException(status_code=403, detail=str(pe))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
