
# from pydantic import BaseModel
# from typing import Optional

# class UserBase(BaseModel):
#     user_name: str
#     user_role_id: int
#     employee_id: Optional[int]

# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int
#     is_active: bool
#     token: Optional[str]  # Field to store JWT token

#     class Config:
#         orm_mode = True

# from pydantic import BaseModel
# from typing import Optional


# class UserBase(BaseModel):
#     user_name: str
#     is_active: Optional[bool] = True
#     token: Optional[str] = None


# class UserCreate(UserBase):
#     password: str
#     employee_id: int
#     user_role_id: int


# class UserUpdate(UserBase):
#     pass


# class UserInDB(UserBase):
#     id: int
#     class Config:
#         orm_mode = True


# from pydantic import BaseModel
# from typing import Optional


# class UserBase(BaseModel):
#     user_name: str
#     is_active: Optional[bool] = True
#     token: Optional[str] = None


# class UserCreate(UserBase):
#     password: str
#     employee_id: int
#     user_role_id: int

from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    user_name: str
    is_active: Optional[bool] = True
    token: Optional[str] = None


class UserCreate(UserBase):
    password: str
    employee_id: int
    user_role_id: int

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: int
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    user_name: str
    password: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

