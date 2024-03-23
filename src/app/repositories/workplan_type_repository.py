from sqlalchemy.orm import Session
from models.all_models import WorkPlanType
from schemas.workplan_type_schema import WorkPlanTypeCreate, WorkPlanType as WorkPlanTypeResponse
from typing import List, Optional

class WorkPlanTypeRepository:
    def __init__(self, db: Session):
        self.session = db

    def get_workplan_type_by_id(self, workplan_type_id: int) -> Optional[WorkPlanTypeResponse]:
        return self.session.query(WorkPlanType).filter(WorkPlanType.id == workplan_type_id,WorkPlanType.is_active==True).first()
    
    def get_all_deleted_workplan_types(self)->List[WorkPlanTypeResponse]:
        return self.session.query(WorkPlanType).filter(WorkPlanType.is_active == False).all()
    
    def get_workplan_type_by_name(self, workplan_type_name: str) -> Optional[WorkPlanTypeResponse]:
        return self.session.query(WorkPlanType).filter(WorkPlanType.workplan_type_name == workplan_type_name, WorkPlanType.is_active==True).first()

    def get_all_workplan_types(self) -> List[WorkPlanTypeResponse]:
        return self.session.query(WorkPlanType).filter(WorkPlanType.is_active == True).all()

    def create_workplan_type(self, workplan_type_create: WorkPlanTypeCreate) -> WorkPlanTypeResponse:
        workplan_type_data = workplan_type_create.dict()
        workplan_type = WorkPlanType(**workplan_type_data)
        self.session.add(workplan_type)
        self.session.commit()
        self.session.refresh(workplan_type)
        return workplan_type

    def update_workplan_type(self, workplan_type_id: int, workplan_type_update: WorkPlanTypeCreate) -> Optional[WorkPlanTypeResponse]:
        workplan_type = self.get_workplan_type_by_id(workplan_type_id)
        if workplan_type:
            workplan_type_data = workplan_type_update.dict(exclude_unset=True)
            for key, value in workplan_type_data.items():
                setattr(workplan_type, key, value)
            self.session.commit()
            self.session.refresh(workplan_type)
        return workplan_type

    def delete_workplan_type(self, workplan_type_id: int) -> bool:
        workplan_type = self.get_workplan_type_by_id(workplan_type_id)
        if workplan_type:
            workplan_type.is_active = False
            self.session.commit()
            return True
        return False
