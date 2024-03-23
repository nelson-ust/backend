# from pydantic import BaseModel
# from typing import Optional


# class UserBase(BaseModel):
#     user_name: str
#     is_active: bool

#     class Config:
#         from_attributes = True


# class UserCreate(UserBase):
#     pass


# class User(UserBase):
#     id: int
#     employee_id: Optional[int] = None
#     user_role_id: Optional[int] = None

#     class Config:
#         from_attributes = True


# class UserWithToken(User):
#     jwt_token: str

#     class Config:
#         from_attributes = True

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    user_name: str
    user_role_id: int
    employee_id: Optional[int]

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    token: Optional[str]  # Field to store JWT token

    class Config:
        orm_mode = True
