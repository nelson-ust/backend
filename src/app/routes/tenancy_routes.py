from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from db.database import get_db
from services.tenancy_service import TenancyService
from schemas.tenancy_schema import (
    TenancyCreate,
    TenancyUpdate,
    TenancyRead,
    TenancyList,
    TenancyDetail,
    TenancyInDB
)

router = APIRouter()


@router.post("/tenancies/", response_model=TenancyInDB,status_code=201)
def create_tenancy(tenancy:TenancyCreate,db:Session=Depends(get_db)):
    tenancy_service=TenancyService(db)
    created_tenancy = tenancy_service.create_tenancy(tenancy)
    if not created_tenancy:
        raise HTTPException(
            status_code=500,
            detail="Failed to create Tenancy. There is a match for this Tenant in the DB",
            headers={"X-Error": "There was an error processing your request."},
        )
    return created_tenancy

@router.get("/tenancies/{tenancy_id}", response_model=TenancyDetail)
def read_tenancy(tenancy_id: int, db: Session = Depends(get_db)):
    tenancy_service=TenancyService(db)
    db_tenancy = tenancy_service.get_tenancy(tenancy_id)
    if db_tenancy is None:
        raise HTTPException(status_code=404, detail="Tenancy not found")
    return {"data": db_tenancy}

@router.get("/tenancies/", response_model=TenancyList)
def read_tenancies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tenancy_service=TenancyService(db)
    tenancies = tenancy_service.get_tenancies(skip, limit)
    return {"data": tenancies}

@router.put("/tenancies/{tenancy_id}", response_model=TenancyDetail)
def update_tenancy(
    tenancy_id: int, tenancy: TenancyUpdate, db: Session = Depends(get_db)
):
    tenancy_service=TenancyService(db)
    db_tenancy = tenancy_service.update_tenancy( tenancy_id, tenancy)
    if db_tenancy is None:
        raise HTTPException(status_code=404, detail="Tenancy not found")
    return {"data": db_tenancy}

@router.delete("/tenancies/{tenancy_id}", response_model=TenancyDetail)
def delete_tenancy(tenancy_id: int, db: Session = Depends(get_db)):
    tenancy_service=TenancyService(db)
    deleted_tenancy = tenancy_service.delete_tenancy(tenancy_id)
    if deleted_tenancy is None:
        raise HTTPException(status_code=404, detail="Tenancy not found")
    return {"data": deleted_tenancy}
