# #app/schemas/tenancy_schema.py
# from pydantic import BaseModel
# from typing import List, Optional
# from datetime import datetime


# class TenancyBase(BaseModel):
#     tenant_name:str

# # Response model for creating a new tenancy
# class TenancyCreate(TenancyBase):
#     pass

# # Response model for reading a tenancy
# class TenancyRead(BaseModel):
#     id: int
#     tenant_name: str
#     is_active: bool
#     date_created: datetime
#     date_updated: Optional[datetime]


# class TenancyInDB(BaseModel):
#     id: int
#     tenancy_name: str

#     class Config:
#         from_attributes = True
# # Response model for updating a tenancy
# class TenancyUpdate(BaseModel):
#     tenant_name: Optional[str]

# # Response model for deleting a tenancy
# class TenancyDelete(BaseModel):
#     message: str = "Tenancy deleted successfully"

# # Response model for tenancy operations that return lists of tenancies
# class TenancyList(BaseModel):
#     data: List[TenancyRead]

# # Response model for tenancy operations that return a single tenancy
# class TenancyDetail(BaseModel):
#     data: TenancyRead

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TenancyBase(BaseModel):
    tenant_name: str

class TenancyCreate(TenancyBase):
    pass

class TenancyUpdate(BaseModel):
    tenant_name: Optional[str]

class TenancyRead(BaseModel):
    id: int
    tenant_name: str
    is_active: bool
    date_created: datetime
    date_updated: Optional[datetime]

class TenancyInDB(TenancyRead):
    class Config:
        from_attributes=True

class TenancyDetail(BaseModel):
    data: TenancyRead

class TenancyList(BaseModel):
    data: list[TenancyRead]
