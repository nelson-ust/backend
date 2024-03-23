from sqlalchemy.orm import Session
from repositories.department_repository import DepartmentRepository
from schemas.department_schema import DepartmentCreate, Department as DepartmentResponse
from typing import List, Optional

class DepartmentService:
    def __init__(self, db: Session):
        self.repository = DepartmentRepository(db)

    def get_department_by_id(self, department_id: int) -> Optional[DepartmentResponse]:
        return self.repository.get_department_by_id(department_id)

    def get_department_by_name(self, dept_name: str) -> Optional[DepartmentResponse]:
        return self.repository.get_department_by_name(dept_name)

    def get_all_departments(self) -> List[DepartmentResponse]:
        return self.repository.get_all_departments()

    def create_department(self, department_create: DepartmentCreate) -> DepartmentResponse:
        return self.repository.create_department(department_create)

    def update_department(self, department_id: int, department_update: DepartmentCreate) -> Optional[DepartmentResponse]:
        return self.repository.update_department(department_id, department_update)

    def delete_department(self, department_id: int) -> bool:
        return self.repository.delete_department(department_id)
