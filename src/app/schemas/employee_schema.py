# #schemas/employee_schema.py
# from pydantic import BaseModel
# from typing import Optional

# class EmployeeBase(BaseModel):
#     first_name: str
#     last_name: str
#     phone_number: str
#     email: str
#     address: str
#     employee_code: str
#     is_unit_lead: Optional[bool] = False
#     is_dept_lead: Optional[bool] = False
#     is_srt_lead: Optional[bool] = False
#     is_stl: Optional[bool] = False
#     is_technical_lead: Optional[bool] = False
#     unit_id: Optional[int]
#     tenancy_id: Optional[int]
#     srt_id: Optional[int]
#     dept_id: Optional[int]

# class EmployeeCreate(EmployeeBase):
#     pass

# class Employee(EmployeeBase):
#     id: int
#     unit_id: Optional[int]
#     tenancy_id: Optional[int]
#     srt_id: Optional[int]
#     dept_id: Optional[int]

#     class Config:
#         from_attributes = True

#schemas/employee_schema.py
from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str
    employee_code: str
    is_unit_lead: Optional[bool] = False
    is_dept_lead: Optional[bool] = False
    is_srt_lead: Optional[bool] = False
    is_stl: Optional[bool] = False
    is_technical_lead: Optional[bool] = False
    unit_id: Optional[int]
    tenancy_id: Optional[int]
    srt_id: Optional[int]
    dept_id: Optional[int]

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
