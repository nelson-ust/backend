
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from services.employee_service import EmployeeService
from schemas.employee_schema import EmployeeCreate, Employee

router = APIRouter()

@router.post("/employees/", response_model=Employee, status_code=201)
def create_employee(employee_data: EmployeeCreate, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    return employee_service.create_employee(employee_data)

@router.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employee = employee_service.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee_data: EmployeeCreate, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employee = employee_service.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_service.update_employee(employee_id, employee_data)

@router.delete("/employees/{employee_id}", response_model=Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employee = employee_service.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_service.delete_employee(employee_id)

@router.get("/employees/by_employee_code/{employee_code}", response_model=Employee)
def get_employee_by_employee_code(employee_code: str, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employee = employee_service.get_employee_by_employee_code(employee_code)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.get("/employees/by_srt_name/{srt_name}", response_model=Employee)
def get_employees_by_srt_name(srt_name: str, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employees = employee_service.get_employees_by_srt_name(srt_name)
    if not employees:
        raise HTTPException(status_code=404, detail="Employees not found")
    return employees

@router.get("/employees/by_tenant_name/{tenant_name}", response_model=Employee)
def get_employees_by_tenant_name(tenant_name: str, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employees = employee_service.get_employees_by_tenant_name(tenant_name)
    if not employees:
        raise HTTPException(status_code=404, detail="Employees not found")
    return employees


@router.get("/employees/by_unit_name/{unit_name}", response_model=Employee)
def get_employees_by_unit_name(unit_name: str, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employees = employee_service.get_employees_by_unit_name(unit_name)
    if not employees:
        raise HTTPException(status_code=404, detail="Employees not found")
    return employees

@router.get("/employees/by_department_name/{department_name}", response_model=Employee)
def get_employees_by_department_name(department_name: str, db: Session = Depends(get_db)):
    employee_service = EmployeeService(db)
    employees = employee_service.get_employees_by_department_name(department_name)
    if not employees:
        raise HTTPException(status_code=404, detail="Employees not found")
    return employees
