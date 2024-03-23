
# routes/srt_routes.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from services.srt_service import SRTService
from schemas.srt_schema import SRTCreate, SRTInDB, SRTUpdate

router = APIRouter()

@router.post("/srts/", response_model=SRTInDB, status_code=201)
def create_srt(srt: SRTCreate, tenancy_id: int, db: Session = Depends(get_db)):
    srt_service = SRTService(db)
    created_srt = srt_service.create_srt(srt, tenancy_id)
    
    if not created_srt:
        raise HTTPException(
            status_code=500,
            detail="Failed to create SRT. There is a match for this SRT with the Choosen Tenant in the DB.",
            headers={"X-Error": "There was an error processing your request."},
        )
    
    return created_srt

@router.get("/srts/{srt_id}", response_model=SRTInDB)
def read_srt(srt_id: int, db: Session = Depends(get_db)):
    srt_service = SRTService(db)
    db_srt = srt_service.get_srt(srt_id)
    if db_srt is None:
        raise HTTPException(status_code=404, detail="SRT not found")
    return db_srt

@router.get("/srts/", response_model=List[SRTInDB])
def read_srts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    srt_service = SRTService(db)
    srts = srt_service.get_srts()  # Utilize the modified get_srts method
    return srts

@router.put("/srts/{srt_id}", response_model=SRTInDB)
def update_srt(srt_id: int, srt: SRTUpdate, db: Session = Depends(get_db)):
    srt_service = SRTService(db)
    db_srt = srt_service.update_srt(srt_id, srt)
    if db_srt is None:
        raise HTTPException(status_code=404, detail="This SRT already exists for the Tenant")
    return db_srt
