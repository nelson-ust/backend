from pydantic import BaseModel

class WorkPlanTypeBase(BaseModel):
    workplan_type_name: str

class WorkPlanTypeCreate(WorkPlanTypeBase):
    pass

class WorkPlanType(WorkPlanTypeBase):
    id: int

    class Config:
        from_attributes = True
