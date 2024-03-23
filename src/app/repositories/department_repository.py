from sqlalchemy.orm import Session
from models.all_models import Department
from schemas.department_schema import DepartmentCreate, Department as DepartmentResponse
from typing import List, Optional

class DepartmentRepository:
    def __init__(self, db: Session):
        self.session = db

    def get_department_by_id(self, department_id: int) -> Optional[DepartmentResponse]:
        return self.session.query(Department).filter(Department.id == department_id,Department.is_active==True).first()

    def get_department_by_name(self, dept_name: str) -> Optional[DepartmentResponse]:
        return self.session.query(Department).filter(Department.dept_name == dept_name,Department.is_active==True).first()

    def get_all_departments(self) -> List[DepartmentResponse]:
        return self.session.query(Department).filter(Department.is_active == True).all()

    def create_department(self, department_create: DepartmentCreate) -> DepartmentResponse:
        department_data = department_create.dict()
        department = Department(**department_data)
        self.session.add(department)
        self.session.commit()
        self.session.refresh(department)
        return department

    def update_department(self, department_id: int, department_update: DepartmentCreate) -> Optional[DepartmentResponse]:
        department = self.get_department_by_id(department_id)
        if department:
            department_data = department_update.dict(exclude_unset=True)
            for key, value in department_data.items():
                setattr(department, key, value)
            self.session.commit()
            self.session.refresh(department)
        return department

    def delete_department(self, department_id: int) -> bool:
        department = self.get_department_by_id(department_id)
        if department:
            department.is_active = False
            self.session.commit()
            return True
        return False
