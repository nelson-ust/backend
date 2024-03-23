from sqlalchemy.orm import Session
from repositories.workplan_type_repository import WorkPlanTypeRepository
from schemas.workplan_type_schema import WorkPlanTypeCreate, WorkPlanType as WorkPlanTypeResponse
from typing import List, Optional

class WorkPlanTypeService:
    def __init__(self, db: Session):
        self.repository = WorkPlanTypeRepository(db)

    def get_workplan_type_by_id(self, workplan_type_id: int) -> Optional[WorkPlanTypeResponse]:
        return self.repository.get_workplan_type_by_id(workplan_type_id)

    def get_workplan_type_by_name(self, workplan_type_name: str) -> Optional[WorkPlanTypeResponse]:
        return self.repository.get_workplan_type_by_name(workplan_type_name)
    
    def get_all_deleted_workplan_types(self) -> List[WorkPlanTypeResponse]:
        return self.repository.get_all_deleted_workplan_types()

    def get_all_workplan_types(self) -> List[WorkPlanTypeResponse]:
        return self.repository.get_all_workplan_types()

    def create_workplan_type(self, workplan_type_create: WorkPlanTypeCreate) -> WorkPlanTypeResponse:
        return self.repository.create_workplan_type(workplan_type_create)

    def update_workplan_type(self, workplan_type_id: int, workplan_type_update: WorkPlanTypeCreate) -> Optional[WorkPlanTypeResponse]:
        return self.repository.update_workplan_type(workplan_type_id, workplan_type_update)

    def delete_workplan_type(self, workplan_type_id: int) -> bool:
        return self.repository.delete_workplan_type(workplan_type_id)
