# from sqlalchemy.orm import Session
# from models.all_models import Location, Tenancy
# from schemas.location_schema import LocationCreate, Location as LocationResponse
# from typing import List, Optional

# class LocationRepository:
#     def __init__(self, db: Session):
#         self.session = db

#     def get_location_by_id(self, location_id: int) -> Optional[LocationResponse]:
#         return self.session.query(Location).filter(Location.id == location_id).first()

#     def get_location_by_name_and_tenancy_id(self, location_name: str, tenancy_id: int) -> Optional[LocationResponse]:
#         return self.session.query(Location).filter(
#             Location.location_name == location_name,
#             Location.tenancy_id == tenancy_id
#         ).first()
    
#     def get_all_locations_with_tenancy_name(self) -> List[LocationResponse]:
#         return self.session.query(Location, Tenancy.tenant_name).join(Tenancy, Location.tenancy_id == Tenancy.id).filter(Location.is_active == True).all()

#     def get_all_locations(self) -> List[LocationResponse]:
#         return self.session.query(Location).filter(Location.is_active == True).all()

#     def create_location(self, location_create: LocationCreate) -> LocationResponse:
#         location_data = location_create.dict()
#         existing_location = self.get_location_by_name_and_tenancy_id(location_data['location_name'], location_data['tenancy_id'])
#         if existing_location:
#             raise ValueError("Location with the same name and tenancy already exists")
        
#         location = Location(**location_data)
#         self.session.add(location)
#         self.session.commit()
#         self.session.refresh(location)
#         return location

#     def update_location(self, location_id: int, location_update: LocationCreate) -> Optional[LocationResponse]:
#         location = self.get_location_by_id(location_id)
#         if location:
#             location_data = location_update.dict(exclude_unset=True)
#             existing_location = self.get_location_by_name_and_tenancy_id(location_data['location_name'], location_data['tenancy_id'])
#             if existing_location and existing_location.id != location_id:
#                 raise ValueError("Location with the same name and tenancy already exists")
            
#             for key, value in location_data.items():
#                 setattr(location, key, value)
#             self.session.commit()
#             self.session.refresh(location)
#         return location

#     def delete_location(self, location_id: int) -> bool:
#         location = self.get_location_by_id(location_id)
#         if location:
#             location.is_active = False
#             self.session.commit()
#             return True
#         return False


from sqlalchemy.orm import Session
from models.all_models import Location, Tenancy
from schemas.location_schema import LocationCreate, LocationWithTenancyResponse
from typing import List, Optional

class LocationRepository:
    def __init__(self, db: Session):
        self.session = db

    def get_location_by_id(self, location_id: int) -> Optional[Location]:
        return self.session.query(Location).filter(Location.id == location_id,Location.is_active==True).first()

    def get_location_by_name_and_tenancy_id(self, location_name: str, tenancy_id: int) -> Optional[Location]:
        return self.session.query(Location).filter(
            Location.location_name == location_name,
            Location.tenancy_id == tenancy_id,Location.is_active==True
        ).first()
    
    def get_all_locations_with_tenancy_name(self) -> List[LocationWithTenancyResponse]:
        locations_with_tenancy = self.session.query(Location, Tenancy.tenant_name).join(
            Tenancy, Location.tenancy_id == Tenancy.id).filter(Location.is_active == True).all()
        
        return [LocationWithTenancyResponse(
            id=location.id,
            location_name=location.location_name,
            tenancy_name=tenancy_name
        ) for location, tenancy_name in locations_with_tenancy]

    def get_all_locations(self) -> List[Location]:
        return self.session.query(Location).filter(Location.is_active == True).all()

    def create_location(self, location_create: LocationCreate) -> Location:
        location_data = location_create.dict()
        existing_location = self.get_location_by_name_and_tenancy_id(location_data['location_name'], location_data['tenancy_id'])
        if existing_location:
            raise ValueError("Location with the same name and tenancy already exists")
        
        location = Location(**location_data)
        self.session.add(location)
        self.session.commit()
        self.session.refresh(location)
        return location

    def update_location(self, location_id: int, location_update: LocationCreate) -> Optional[Location]:
        location = self.get_location_by_id(location_id)
        if location:
            location_data = location_update.dict(exclude_unset=True)
            existing_location = self.get_location_by_name_and_tenancy_id(location_data['location_name'], location_data['tenancy_id'])
            if existing_location and existing_location.id != location_id:
                raise ValueError("Location with the same name and tenancy already exists")
            
            for key, value in location_data.items():
                setattr(location, key, value)
            self.session.commit()
            self.session.refresh(location)
        return location

    def delete_location(self, location_id: int) -> bool:
        location = self.get_location_by_id(location_id)
        if location:
            location.is_active = False
            self.session.commit()
            return True
        return False
