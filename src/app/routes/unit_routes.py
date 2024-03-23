from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from services.unit_service import UnitService
from schemas.unit_schema import UnitCreate, Unit

router = APIRouter()


@router.get("/units/", response_model=List[Unit])
def get_units_with_department_names(db: Session = Depends(get_db)):
    unit_service = UnitService(db)
    return unit_service.get_units_with_department_names()


@router.get("/units/{department_name}", response_model=List[Unit])
def get_units_by_department_name(department_name: str, db: Session = Depends(get_db)):
    unit_service = UnitService(db)
    return unit_service.get_units_by_department_name(department_name)


@router.get("/units/{unit_id}/detail", response_model=Unit)
def get_unit_with_department_name_by_id(unit_id: int, db: Session = Depends(get_db)):
    unit_service = UnitService(db)
    unit_detail = unit_service.get_unit_with_department_name_by_id(unit_id)
    if not unit_detail:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit_detail


@router.post("/units/", response_model=Unit, status_code=201)
def create_unit(unit_data: UnitCreate, db: Session = Depends(get_db)):
    unit_service = UnitService(db)
    return unit_service.create_unit(unit_data)


@router.put("/{unit_id}", response_model=Unit)
def update_unit(unit_id: int, unit_data: UnitCreate, db: Session = Depends(get_db)):
    unit_service = UnitService(db)
    unit = unit_service.update_unit(unit_id, unit_data)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit


@router.delete("/{unit_id}", response_model=Unit)
def delete_unit(unit_id: int, db: Session = Depends(get_db)):
    unit_service = UnitService(db)
    unit = unit_service.delete_unit(unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit
