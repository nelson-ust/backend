
# #services/employee_service.py
# from sqlalchemy.orm import Session
# from repositories.employee_repository import EmployeeRepository
# from schemas.employee_schema import EmployeeCreate, Employee

# class EmployeeService:
#     def __init__(self, db_session: Session):
#         self.db_session = db_session
#         self.employee_repo = EmployeeRepository(db_session)

#     def create_employee(self, employee_data: EmployeeCreate) -> Employee:
#         return self.employee_repo.create_employee(employee_data)

#     def get_employee(self, employee_id: int) -> Employee:
#         return self.employee_repo.get_employee(employee_id)

#     def update_employee(self, employee_id: int, employee_data: EmployeeCreate) -> Employee:
#         return self.employee_repo.update_employee(employee_id, employee_data)

#     def delete_employee(self, employee_id: int) -> Employee:
#         return self.employee_repo.delete_employee(employee_id)

#     def get_employee_by_employee_code(self, employee_code: str) -> Employee:
#         return self.employee_repo.get_employee_by_employee_code(employee_code)

#     def get_employees_by_srt_name(self, srt_name: str) -> Employee:
#         return self.employee_repo.get_employees_by_srt_name(srt_name)

#     def get_employees_by_tenant_name(self, tenant_name: str) -> Employee:
#         return self.employee_repo.get_employees_by_tenant_name(tenant_name)

#     def get_employees_by_unit_name(self, unit_name: str) -> Employee:
#         return self.employee_repo.get_employees_by_unit_name(unit_name)

#     def get_employees_by_department_name(self, department_name: str) -> Employee:
#         return self.employee_repo.get_employees_by_department_name(department_name)


from sqlalchemy.orm import Session
from repositories.employee_repository import EmployeeRepository
from schemas.employee_schema import EmployeeCreate, Employee as EmployeeResponse
from typing import List, Optional

class EmployeeService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.employee_repo = EmployeeRepository(db_session)

    def create_employee(self, employee: EmployeeCreate) -> EmployeeResponse:
        return self.employee_repo.create_employee(employee)

    def update_employee(self, employee_id: int, employee_data: EmployeeCreate) -> Optional[EmployeeResponse]:
        return self.employee_repo.update_employee(employee_id, employee_data)

    def get_employee(self, employee_id: int) -> Optional[EmployeeResponse]:
        return self.employee_repo.get_employee(employee_id)

    def delete_employee(self, employee_id: int) -> Optional[EmployeeResponse]:
        return self.employee_repo.delete_employee(employee_id)

    def get_employees_by_employee_code(self, employee_code: str) -> List[EmployeeResponse]:
        return self.employee_repo.get_employee_by_employee_code(employee_code)

    def get_employees_by_srt_name(self, srt_name: str) -> List[EmployeeResponse]:
        return self.employee_repo.get_employees_by_srt_name(srt_name)

    def get_employees_by_tenant_name(self, tenant_name: str) -> List[EmployeeResponse]:
        return self.employee_repo.get_employees_by_tenant_name(tenant_name)

    def get_employees_by_unit_name(self, unit_name: str) -> List[EmployeeResponse]:
        return self.employee_repo.get_employees_by_unit_name(unit_name)

    def get_employees_by_department_name(self, department_name: str) -> List[EmployeeResponse]:
        return self.employee_repo.get_employees_by_department_name(department_name)
