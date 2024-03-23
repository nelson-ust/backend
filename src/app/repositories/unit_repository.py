from sqlalchemy.orm import Session
from models.all_models import Unit, Department
from schemas.unit_schema import UnitCreate
from typing import List


class UnitRepository:
    def __init__(self, db: Session):
        self.session = db

    def get_units_with_department_names(self):
        return self.session.query(Unit.id, Unit.unit_name, Department.dept_name)\
            .join(Department, Department.id == Unit.dept_id)\
            .all()

    def get_units_by_department_name(self, department_name: str) -> List[Unit]:
        return self.session.query(Unit)\
            .join(Department, Department.id == Unit.dept_id)\
            .filter(Department.dept_name == department_name)\
            .all()

    def get_unit_with_department_name_by_id(self, unit_id: int):
        return self.session.query(Unit, Department.dept_name)\
            .join(Department, Department.id == Unit.dept_id)\
            .filter(Unit.id == unit_id)\
            .first()

    def create_unit(self, unit_data: UnitCreate):
        if self.session.query(Unit).filter(Unit.unit_name == unit_data.unit_name).first():
            raise ValueError("Unit with this name already exists.")

        unit = Unit(**unit_data.dict())
        self.session.add(unit)
        self.session.commit()
        self.session.refresh(unit)
        return unit

    def update_unit(self, unit_id: int, unit_data: UnitCreate):
        unit = self.session.query(Unit).filter(Unit.id == unit_id).first()
        if not unit:
            raise ValueError("Unit not found.")

        existing_unit_with_same_name = self.session.query(Unit)\
            .filter(Unit.unit_name == unit_data.unit_name, Unit.id != unit_id).first()
        if existing_unit_with_same_name:
            raise ValueError("Another unit with this name already exists.")

        for attr, value in unit_data.dict().items():
            setattr(unit, attr, value)

        self.session.commit()
        self.session.refresh(unit)
        return unit

    def delete_unit(self, unit_id: int):
        unit = self.session.query(Unit).filter(Unit.id == unit_id).first()
        if not unit:
            raise ValueError("Unit not found.")
        
        self.session.delete(unit)
        self.session.commit()
        return unit
