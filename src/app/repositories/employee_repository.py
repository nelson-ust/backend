
# #repositories/employee_repository.py
# from sqlalchemy.orm import Session
# from models.all_models import Employee, Unit, SRT, Tenancy, Department
# from schemas.employee_schema import EmployeeCreate, Employee


# class EmployeeRepository:
#     def __init__(self, session: Session):
#         self.session = session

#     def create_employee(self, employee: EmployeeCreate):
#         # Check if employee_code and email are unique
#         if self.session.query(Employee).filter(Employee.employee_code == employee.employee_code).first():
#             raise ValueError("Employee with this employee_code already exists.")
#         if self.session.query(Employee).filter(Employee.email == employee.email).first():
#             raise ValueError("Employee with this email already exists.")

#         db_employee = Employee(**employee.dict())
#         self.session.add(db_employee)
#         self.session.commit()
#         self.session.refresh(db_employee)
#         return db_employee

#     def update_employee(self, employee_id: int, employee_data: EmployeeCreate):
#         # Check if employee_code and email are unique for other records
#         existing_employee = self.session.query(Employee).filter(Employee.id != employee_id)
#         if existing_employee.filter(Employee.employee_code == employee_data.employee_code).first():
#             raise ValueError("Employee with this employee_code already exists.")
#         if existing_employee.filter(Employee.email == employee_data.email).first():
#             raise ValueError("Employee with this email already exists.")

#         db_employee = self.get_employee(employee_id)
#         if db_employee:
#             for key, value in employee_data.dict().items():
#                 setattr(db_employee, key, value)
#             self.session.commit()
#             self.session.refresh(db_employee)
#         return db_employee

#     def get_employee(self, employee_id: int):
#         return (
#             self.session.query(Employee, Unit.unit_name, SRT.srt_name, Tenancy.tenant_name, Department.dept_name)
#             .join(Unit, Employee.unit_id == Unit.id, isouter=True)
#             .join(SRT, Employee.srt_id == SRT.id, isouter=True)
#             .join(Tenancy, Employee.tenancy_id == Tenancy.id, isouter=True)
#             .join(Department, Employee.dept_id == Department.id, isouter=True)
#             .filter(Employee.id == employee_id)
#             .first()
#         )

#     def delete_employee(self, employee_id: int):
#         db_employee = self.get_employee(employee_id)
#         if db_employee:
#             db_employee.is_active = False  # Soft delete by setting is_active to False
#             self.session.commit()
#         return db_employee

#     def get_employee_by_employee_code(self, employee_code: str):
#         return self.session.query(Employee).filter(Employee.employee_code == employee_code).first()

#     def get_employees_by_srt_name(self, srt_name: str):
#         return (
#             self.session.query(Employee)
#             .join(SRT, Employee.srt_id == SRT.id)
#             .filter(SRT.srt_name == srt_name)
#             .all()
#         )

#     def get_employees_by_tenant_name(self, tenant_name: str):
#         return (
#             self.session.query(Employee)
#             .join(Tenancy, Employee.tenancy_id == Tenancy.id)
#             .filter(Tenancy.tenant_name == tenant_name)
#             .all()
#         )

#     def get_employees_by_unit_name(self, unit_name: str):
#         return (
#             self.session.query(Employee)
#             .join(Unit, Employee.unit_id == Unit.id)
#             .filter(Unit.unit_name == unit_name)
#             .all()
#         )

#     def get_employees_by_department_name(self, department_name: str):
#         return (
#             self.session.query(Employee)
#             .join(Department, Employee.dept_id == Department.id)
#             .filter(Department.dept_name == department_name)
#             .all()
#         )


from sqlalchemy.orm import Session
from models.all_models import SRT, Department, Employee, Tenancy, Unit
from schemas.employee_schema import EmployeeCreate, Employee as EmployeeResponse
from typing import List, Optional

class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    # def create_employee(self, employee: EmployeeCreate) -> EmployeeResponse:
    #     db_employee = Employee(**employee.dict())
    #     self.session.add(db_employee)
    #     self.session.commit()
    #     self.session.refresh(db_employee)
    #     return db_employee

    def create_employee(self, employee: EmployeeCreate) -> Optional[EmployeeResponse]:
        # Check if employee_code and email are unique
        if self.session.query(Employee).filter(Employee.employee_code == employee.employee_code).first():
            raise ValueError("Employee with this employee_code already exists.")
        if self.session.query(Employee).filter(Employee.email == employee.email).first():
            raise ValueError("Employee with this email already exists.")
        
        # Create the new employee record
        db_employee = Employee(**employee.dict())
        self.session.add(db_employee)
        self.session.commit()
        self.session.refresh(db_employee)
        return db_employee

    def update_employee(self, employee_id: int, employee_data: EmployeeCreate) -> Optional[EmployeeResponse]:
        db_employee = self.get_employee(employee_id)
        if db_employee:
            employee_data = employee_data.dict(exclude_unset=True)
            for key, value in employee_data.items():
                setattr(db_employee, key, value)
            self.session.commit()
            self.session.refresh(db_employee)
        return db_employee

    def get_employee(self, employee_id: int) -> Optional[EmployeeResponse]:
        return self.session.query(Employee).filter(Employee.id == employee_id).first()

    def delete_employee(self, employee_id: int) -> Optional[EmployeeResponse]:
        db_employee = self.get_employee(employee_id)
        if db_employee:
            self.session.delete(db_employee)
            self.session.commit()
        return db_employee

    def get_employee_by_employee_code(self, employee_code: str) -> List[EmployeeResponse]:
        return self.session.query(Employee).filter(Employee.employee_code == employee_code).all()

    def get_employees_by_srt_name(self, srt_name: str) -> List[EmployeeResponse]:
        return (
            self.session.query(Employee)
            .join(Employee.srt)
            .filter(SRT.srt_name == srt_name)
            .all()
        )

    def get_employees_by_tenant_name(self, tenant_name: str) -> List[EmployeeResponse]:
        return (
            self.session.query(Employee)
            .join(Employee.tenancy)
            .filter(Tenancy.tenant_name == tenant_name)
            .all()
        )

    def get_employees_by_unit_name(self, unit_name: str) -> List[EmployeeResponse]:
        return (
            self.session.query(Employee)
            .join(Employee.unit)
            .filter(Unit.unit_name == unit_name)
            .all()
        )

    def get_employees_by_department_name(self, department_name: str) -> List[EmployeeResponse]:
        return (
            self.session.query(Employee)
            .join(Employee.department)
            .filter(Department.dept_name == department_name)
            .all()
        )
