# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from schemas.user_schema import User, UserCreate
# from services.user_service import UserService
# from db.database import get_db

# router = APIRouter(prefix="/users", tags=["users"])


# @router.get("/{user_id}", response_model=User)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = UserService(db).get_user_by_id(user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# @router.post("/", response_model=User)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     return UserService(db).create_user(user)


# @router.put("/{user_id}", response_model=User)
# def update_user(user_id: int, user_data: dict, db: Session = Depends(get_db)):
#     updated_user = UserService(db).update_user(user_id, user_data)
#     if updated_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return updated_user


# @router.delete("/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     deleted_user = UserService(db).delete_user(user_id)
#     if deleted_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return {"message": "User deleted successfully"}


# @router.get("/active", response_model=list[User])
# def get_all_active_users(db: Session = Depends(get_db)):
#     return UserService(db).get_all_active_users()


# @router.get("/inactive", response_model=list[User])
# def get_all_inactive_users(db: Session = Depends(get_db)):
#     return UserService(db).get_all_inactive_users()


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user_service import UserService
from schemas.user_schema import UserCreate, User
from db.database import get_db

router = APIRouter()

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserService(db).get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", response_model=list[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return UserService(db).get_users(skip, limit)

@router.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_data: dict, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, user_data)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user(user_id)

@router.get("/users/active", response_model=list[User])
def get_all_active_users(db: Session = Depends(get_db)):
    return UserService(db).get_all_active_users()

@router.get("/users/inactive", response_model=list[User])
def get_all_inactive_users(db: Session = Depends(get_db)):
    return UserService(db).get_all_inactive_users()

@router.get("/users/{user_id}/email", response_model=str)
def get_user_email(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user_email(user_id)
