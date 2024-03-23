from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.department_schema import DepartmentCreate, Department as DepartmentResponse
from services.department_service import DepartmentService

#router = APIRouter(prefix="/departments", tags=["departments"])
router = APIRouter()

@router.get("/departments/", response_model=List[DepartmentResponse])
def get_all_departments(db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    return department_service.get_all_departments()

@router.get("/departments/{department_id}", response_model=DepartmentResponse)
def get_department_by_id(department_id: int, db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    department = department_service.get_department_by_id(department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@router.post("/departments/", response_model=DepartmentResponse, status_code=201)
def create_department(department_create: DepartmentCreate, db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    return department_service.create_department(department_create)

@router.put("/departments/{department_id}", response_model=DepartmentResponse)
def update_department(department_id: int, department_update: DepartmentCreate, db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    department = department_service.update_department(department_id, department_update)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department

@router.delete("/departments/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    department_service = DepartmentService(db)
    if not department_service.delete_department(department_id):
        raise HTTPException(status_code=404, detail="Department not found")
    return {"message": "Department deleted successfully"}
