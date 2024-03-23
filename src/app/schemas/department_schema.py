from pydantic import BaseModel

class DepartmentBase(BaseModel):
    dept_name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int

    class Config:
        from_attributes=True
