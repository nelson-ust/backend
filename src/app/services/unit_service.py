from sqlalchemy.orm import Session
from repositories.unit_repository import UnitRepository
from schemas.unit_schema import UnitCreate, Unit
from typing import List


class UnitService:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.unit_repo = UnitRepository(db_session)

    def get_units_with_department_names(self):
        return self.unit_repo.get_units_with_department_names()

    def get_units_by_department_name(self, department_name: str) -> List[Unit]:
        return self.unit_repo.get_units_by_department_name(department_name)

    def get_unit_with_department_name_by_id(self, unit_id: int):
        return self.unit_repo.get_unit_with_department_name_by_id(unit_id)

    def create_unit(self, unit_data: UnitCreate) -> Unit:
        return self.unit_repo.create_unit(unit_data)

    def update_unit(self, unit_id: int, unit_data: UnitCreate) -> Unit:
        return self.unit_repo.update_unit(unit_id, unit_data)

    def delete_unit(self, unit_id: int) -> Unit:
        return self.unit_repo.delete_unit(unit_id)
