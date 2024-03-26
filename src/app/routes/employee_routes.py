
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from db.database import get_db
# from services.employee_service import EmployeeService
# from schemas.employee_schema import EmployeeCreate, Employee

# router = APIRouter()

# @router.post("/employees/", response_model=Employee, status_code=201)
# def create_employee(employee_data: EmployeeCreate, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     return employee_service.create_employee(employee_data)

# @router.get("/employees/{employee_id}", response_model=Employee)
# def get_employee(employee_id: int, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employee = employee_service.get_employee(employee_id)
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee

# @router.put("/employees/{employee_id}", response_model=Employee)
# def update_employee(employee_id: int, employee_data: EmployeeCreate, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employee = employee_service.get_employee(employee_id)
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee_service.update_employee(employee_id, employee_data)

# @router.delete("/employees/{employee_id}", response_model=Employee)
# def delete_employee(employee_id: int, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employee = employee_service.get_employee(employee_id)
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee_service.delete_employee(employee_id)

# @router.get("/employees/by_employee_code/{employee_code}", response_model=Employee)
# def get_employee_by_employee_code(employee_code: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employee = employee_service.get_employee_by_employee_code(employee_code)
#     if not employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee

# @router.get("/employees/by_srt_name/{srt_name}", response_model=Employee)
# def get_employees_by_srt_name(srt_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_srt_name(srt_name)
#     if not employees:
#         raise HTTPException(status_code=404, detail="Employees not found")
#     return employees

# @router.get("/employees/by_tenant_name/{tenant_name}", response_model=Employee)
# def get_employees_by_tenant_name(tenant_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_tenant_name(tenant_name)
#     if not employees:
#         raise HTTPException(status_code=404, detail="Employees not found")
#     return employees


# @router.get("/employees/by_unit_name/{unit_name}", response_model=Employee)
# def get_employees_by_unit_name(unit_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_unit_name(unit_name)
#     if not employees:
#         raise HTTPException(status_code=404, detail="Employees not found")
#     return employees

# @router.get("/employees/by_department_name/{department_name}", response_model=Employee)
# def get_employees_by_department_name(department_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_department_name(department_name)
#     if not employees:
#         raise HTTPException(status_code=404, detail="Employees not found")
#     return employees


# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from db.database import get_db
# from services.employee_service import EmployeeService
# from schemas.employee_schema import EmployeeCreate, Employee as EmployeeResponse
# from typing import List

# router = APIRouter()

# @router.post("/employees/", response_model=EmployeeResponse)
# def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     return employee_service.create_employee(employee)

# @router.put("/employees/{employee_id}", response_model=EmployeeResponse)
# def update_employee(employee_id: int, employee_data: EmployeeCreate, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     updated_employee = employee_service.update_employee(employee_id, employee_data)
#     if updated_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return updated_employee

# @router.get("/employees/{employee_id}", response_model=EmployeeResponse)
# def get_employee(employee_id: int, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employee = employee_service.get_employee(employee_id)
#     if employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee

# @router.delete("/employees/{employee_id}", response_model=EmployeeResponse)
# def delete_employee(employee_id: int, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     deleted_employee = employee_service.delete_employee(employee_id)
#     if deleted_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return deleted_employee

# @router.get("/employees/by_employee_code/{employee_code}", response_model=List[EmployeeResponse])
# def get_employees_by_employee_code(employee_code: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_employee_code(employee_code)
#     return employees

# @router.get("/employees/by_srt_name/{srt_name}", response_model=List[EmployeeResponse])
# def get_employees_by_srt_name(srt_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_srt_name(srt_name)
#     return employees

# @router.get("/employees/by_tenant_name/{tenant_name}", response_model=List[EmployeeResponse])
# def get_employees_by_tenant_name(tenant_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_tenant_name(tenant_name)
#     return employees

# @router.get("/employees/by_unit_name/{unit_name}", response_model=List[EmployeeResponse])
# def get_employees_by_unit_name(unit_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_unit_name(unit_name)
#     return employees

# @router.get("/employees/by_department_name/{department_name}", response_model=List[EmployeeResponse])
# def get_employees_by_department_name(department_name: str, db: Session = Depends(get_db)):
#     employee_service = EmployeeService(db)
#     employees = employee_service.get_employees_by_department_name(department_name)
#     return employees

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.employee_schema import EmployeeCreate, Employee as EmployeeResponse
from services.employee_service import EmployeeService
from db.database import get_db

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=EmployeeResponse)
async def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        return EmployeeService(db).create_employee(employee)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.get("/{employee_id}", response_model=EmployeeResponse)
async def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = EmployeeService(db).get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}", response_model=EmployeeResponse)
async def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        return EmployeeService(db).update_employee(employee_id, employee)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{employee_id}", response_model=EmployeeResponse)
async def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        return EmployeeService(db).delete_employee(employee_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/", response_model=List[EmployeeResponse])
async def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return EmployeeService(db).get_employees(skip, limit)

@router.get("/by_department/{department_name}", response_model=List[EmployeeResponse])
async def get_employees_by_department(department_name: str, db: Session = Depends(get_db)):
    try:
        return EmployeeService(db).get_employees_by_department(department_name)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/by_unit/{unit_name}", response_model=List[EmployeeResponse])
async def get_employees_by_unit(unit_name: str, db: Session = Depends(get_db)):
    try:
        return EmployeeService(db).get_employees_by_unit(unit_name)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/by_srt/{srt_name}", response_model=List[EmployeeResponse])
async def get_employees_by_srt(srt_name: str, db: Session = Depends(get_db)):
    try:
        return EmployeeService(db).get_employees_by_srt(srt_name)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
