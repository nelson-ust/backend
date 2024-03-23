from sqlalchemy.orm import Session
from repositories.location_repository import LocationRepository
from schemas.location_schema import LocationCreate, Location as LocationResponse,LocationWithTenancyResponse
from typing import List, Optional

class LocationService:
    def __init__(self, session: Session):
        self.repository = LocationRepository(session)

    def get_location_by_id(self, location_id: int) -> Optional[LocationResponse]:
        return self.repository.get_location_by_id(location_id)

    def get_all_locations(self) -> List[LocationResponse]:
        return self.repository.get_all_locations()

    def get_all_locations_with_tenancy_name(self) -> List[LocationWithTenancyResponse]:
        return self.repository.get_all_locations_with_tenancy_name()

    def create_location(self, location_create: LocationCreate) -> LocationResponse:
        return self.repository.create_location(location_create)

    def update_location(self, location_id: int, location_update: LocationCreate) -> Optional[LocationResponse]:
        return self.repository.update_location(location_id, location_update)

    def delete_location(self, location_id: int) -> bool:
        return self.repository.delete_location(location_id)
