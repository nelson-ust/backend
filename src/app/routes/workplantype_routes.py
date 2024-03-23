from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from schemas.workplan_type_schema import WorkPlanTypeCreate, WorkPlanType as WorkPlanTypeResponse
from services.workplan_type_service import WorkPlanTypeService
from db.database import get_db

# router = APIRouter (prefix="/workplan_types", tags=["workplan_types"])
router = APIRouter()
@router.get("/workplan_types/", response_model=List[WorkPlanTypeResponse])
def get_all_workplan_types(db: Session = Depends(get_db)):
    workplan_type_service = WorkPlanTypeService(db)
    return workplan_type_service.get_all_workplan_types()

@router.get("/workplan_types/", response_model=List[WorkPlanTypeResponse])
def get_all_deleted_workplan_types(db:Session= Depends(get_db)):
    workpla_type_service = WorkPlanTypeService(db)
    return workpla_type_service.get_all_deleted_workplan_types()

@router.get("/workplan_types/{workplan_type_id}", response_model=WorkPlanTypeResponse)
def get_workplan_type_by_id(workplan_type_id: int, db: Session = Depends(get_db)):
    workplan_type_service = WorkPlanTypeService(db)
    workplan_type = workplan_type_service.get_workplan_type_by_id(workplan_type_id)
    if not workplan_type:
        raise HTTPException(status_code=404, detail="Work Plan Type not found")
    return workplan_type

@router.post("/workplan_types/", response_model=WorkPlanTypeResponse, status_code=201)
def create_workplan_type(workplan_type_create: WorkPlanTypeCreate, db: Session = Depends(get_db)):
    workplan_type_service = WorkPlanTypeService(db)
    return workplan_type_service.create_workplan_type(workplan_type_create)

@router.put("/workplan_types/{workplan_type_id}", response_model=WorkPlanTypeResponse)
def update_workplan_type(workplan_type_id: int, workplan_type_update: WorkPlanTypeCreate, db: Session = Depends(get_db)):
    workplan_type_service = WorkPlanTypeService(db)
    workplan_type = workplan_type_service.update_workplan_type(workplan_type_id, workplan_type_update)
    if not workplan_type:
        raise HTTPException(status_code=404, detail="Work Plan Type not found")
    return workplan_type

@router.delete("/workplan_types/{workplan_type_id}")
def delete_workplan_type(workplan_type_id: int, db: Session = Depends(get_db)):
    workplan_type_service = WorkPlanTypeService(db)
    if not workplan_type_service.delete_workplan_type(workplan_type_id):
        raise HTTPException(status_code=404, detail="Work Plan Type not found")
    return {"message": "Work Plan Type deleted successfully"}
