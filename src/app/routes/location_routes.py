from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.location_schema import LocationCreate, Location as LocationResponse,LocationWithTenancyResponse
from services.location_service import LocationService

router = APIRouter()

@router.get("/locations/", response_model=List[LocationResponse])
def get_all_locations(session: Session = Depends(get_db)):
    location_service = LocationService(session)
    return location_service.get_all_locations()

@router.get("/locations/with_tenancy_name", response_model=List[LocationWithTenancyResponse])
def get_all_locations_with_tenancy_name(session: Session = Depends(get_db)):
    location_service = LocationService(session)
    return location_service.get_all_locations_with_tenancy_name()

@router.get("/locations/{location_id}", response_model=LocationResponse)
def get_location_by_id(location_id: int, session: Session = Depends(get_db)):
    location_service = LocationService(session)
    location = location_service.get_location_by_id(location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.post("/locations/", response_model=LocationResponse, status_code=201)
def create_location(location_create: LocationCreate, session: Session = Depends(get_db)):
    location_service = LocationService(session)
    return location_service.create_location(location_create)

@router.put("/locations/{location_id}", response_model=LocationResponse)
def update_location(location_id: int, location_update: LocationCreate, session: Session = Depends(get_db)):
    location_service = LocationService(session)
    location = location_service.update_location(location_id, location_update)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.delete("/locations/{location_id}")
def delete_location(location_id: int, session: Session = Depends(get_db)):
    location_service = LocationService(session)
    if not location_service.delete_location(location_id):
        raise HTTPException(status_code=404, detail="Location not found")
    return {"message": "Location deleted successfully"}
