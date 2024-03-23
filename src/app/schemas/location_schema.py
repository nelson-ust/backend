from pydantic import BaseModel

class LocationBase(BaseModel):
    location_name: str
    tenancy_id: int

class LocationWithTenancyResponse(BaseModel):
    id: int
    location_name: str
    tenancy_name: str
    
class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        from_attributes=True
